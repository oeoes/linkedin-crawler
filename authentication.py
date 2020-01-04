import requests
import config


class Auhentication:

    session = requests.Session()

    def __init__(self, login_url, session_key, session_password, csrf_token):
        self.login_url = login_url
        self.session_key = session_key
        self.session_password = session_password
        self.csrfToken = csrf_token
        self.login()

    def login(self):
        data = {
            'session_key': self.session_key,
            'session_password': self.session_password,
            'csrfToken': self.csrfToken,
            'referer': 'https://www.linkedin.com/'
        }
        try:
            Auhentication.session.post(self.login_url, data=data, headers=config.payload)
        except:
            print('Connection Error. :(')
            exit(1)

    @staticmethod
    def get_cookies():
        cookies = Auhentication.session.cookies.get_dict()
        str_cookie = ''
        for i in cookies:
            str_cookie += (str(i) + "=" + str(cookies.get(i)) + "; ")
        return str_cookie

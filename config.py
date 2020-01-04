
PROJECT_NAME = ''

# Urls
LOGIN_URL = 'https://www.linkedin.com/uas/checkpoint/lg/login-submit'
FEED_URL = 'https://www.linkedin.com/mwlite/getFeeds/?'
CONNECTIONS_URL = 'https://www.linkedin.com/voyager/api/relationships/connections?'
ACCOUNT_URL = 'https://www.linkedin.com/voyager/api/identity/profiles/'

USER_AGENT = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36'
USERNAME = ''
PASSWORD = ''

# Variable yg perlu pembaruan berkala
CSRF_TOKEN = 'ajax:2508282075017288052'
FEED_COOKIE =''
PAGINATION_TOKEN = '612001978-1577811980414-a8b14b6f297ef72b4d2dc687ebdc346b'

payload = {
        'csrf-token': CSRF_TOKEN,
        'user-agent': USER_AGENT,
        'cookie': FEED_COOKIE,
    }

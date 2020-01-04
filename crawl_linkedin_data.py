import config
from authentication import Auhentication
from bs4 import BeautifulSoup
import json
import toolkit


class CrawlLinkedInData(Auhentication):

    connection_list_urls = set()

    def __init__(self):
        super().__init__(config.LOGIN_URL, config.USERNAME, config.PASSWORD, config.CSRF_TOKEN)
        toolkit.create_project_dir(config.PROJECT_NAME)
        CrawlLinkedInData.connection_list_urls = toolkit.cached_file_to_set(config.PROJECT_NAME + '/cached.txt')

    @staticmethod
    def get_feed():
        payload_feed = config.payload
        param = {
            'paginationToken': config.PAGINATION_TOKEN,
            'pageNumber': 1
        }
        req = CrawlLinkedInData.session.get(config.FEED_URL, headers=payload_feed, params=param)
        return req.content.decode('utf-8')

    @staticmethod
    def get_connected_people(start):
        """
        Get data from linkedin users that already connected to our account
        staging = [firsName, lastName, occupation, publicIdentifier, pictureUrl, email, website, phone]
        :param start:
        :return:
        """
        staging = []
        param = {
            'count': 1,
            'start': start,
            'sortType': 'RECENTLY_ADDED'
        }
        try:
            req = CrawlLinkedInData.session.get(config.CONNECTIONS_URL, headers=config.payload, params=param)
            soup = BeautifulSoup(req.content, 'html.parser')
            sp = json.loads(str(soup))
            profile = sp['elements'][0]['miniProfile']
            staging.extend([
                profile['firstName'],
                profile['lastName'],
                profile['occupation'].replace(';', ''),
                profile['publicIdentifier'],
            ])
            try:
                staging.append(profile['picture']['com.linkedin.common.VectorImage']['rootUrl'])
            except KeyError:
                staging.append('-')

            if staging[3] not in CrawlLinkedInData.connection_list_urls:
                CrawlLinkedInData.connection_list_urls.add(staging[3])
                toolkit.append_to_cached_file(config.PROJECT_NAME + '/cached.txt', staging[3])

                CrawlLinkedInData.get_detail_info(staging[3], staging)
                toolkit.append_to_file(config.PROJECT_NAME + '/result.csv', staging)
                print(staging[3])
        except IndexError:
            print('Completed.')
            return False

    @staticmethod
    def get_detail_info(public_identifier, staged_data):
        """
        Get contact info using username url : public_identifier
        :param public_identifier:
        :param staged_data:
        :return:
        """
        req = CrawlLinkedInData.session.get(config.ACCOUNT_URL + public_identifier + '/profileContactInfo',
                                            headers=config.payload)
        soup = json.loads(str(BeautifulSoup(req.content, 'html.parser').decode('utf-8')))

        try:
            staged_data.append(soup['emailAddress'])
        except KeyError:
            staged_data.append('-')

        try:
            staged_data.append(soup['websites'][0]['url'])
        except KeyError:
            staged_data.append('-')

        try:
            staged_data.append(soup['phoneNumbers'][0]['number'])
        except KeyError:
            staged_data.append('-')

        staged_data[3] = 'https://www.linkedin.com/in/' + staged_data[3] + '/'

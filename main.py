from crawl_linkedin_data import CrawlLinkedInData
import config

if __name__ == '__main__':
    cr = CrawlLinkedInData()
    i = 1
    print('Start crawling...')
    while True:
        loop = cr.get_connected_people(i)
        i += 1
        if loop is False:
            break
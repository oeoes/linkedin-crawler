
PROJECT_NAME = 'Crawl_test'

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
FEED_COOKIE = 'li_sugr=0d3773f7-f994-4775-81a8-c4b374fe67a6; bcookie="v=2&42b5ad40-3373-4e4f-852d-c46304ab3106"; bscookie="v=1&201911291549047de23719-de7d-4b15-8b40-a0e011302d6cAQGMwfE9iPIfTgbnaG2ZsU8zUDolXViD"; _ga=GA1.2.741941190.1577419940; VID=V_2019_12_27_04_125; lissc1=1; lissc2=1; fid=AQH5wDZXpU-vdgAAAW9GJvzQT0YnDYMInYjJ3qvUII4ZPH5OdNTlSF5KCDyK3uknwoiab8IeVTINNg; li_at=AQEDASR6aLoAXt_JAAABb1Xc5fgAAAFveelp-E0AjJ_JHoza0KJRrHRld7-aIW-gPOqddI2Oq6mqmpAHeUbp2ojgBSdi25DHHpWPBYu6hvxPLw0vLpUe6XZYLU4AOmelJZwcMKWCbDLHeAheKRbyeSaX; liap=true; JSESSIONID="ajax:2508282075017288052"; li_oatml=AQH7DQCotTe8rwAAAW9V3StVemRCe1aVXPCZUSx8OMj2epZdZbkZEi8Az20bUVneSWqPfpBID3QbVi9nIycKWAIEBbstFM87; _guid=e2ad337b-9620-4e08-b7ef-a98fb73f948d; ac_L=1; ac_LD=1577779459689; pushPermState=default; pushPermInfo=ft=1577780983892&fc=1; lang=v=2&lang=en-us; spectroscopyId=e4705b78-697a-471b-8d52-5da59ed8415e; _lipt=CwEAAAFvXOw98yhPOTyzIWDT7BN-bSrfcTsl-BPBiQIQu9NmaOB7SHIKCH1rhUU2_m1uL_9K7yApE-gxG6z_DAAHVzLYXy4DChbJD0OmwvS23eHoYfPi4gWZPVjL2kslE0VI8KAmXGIGdLueeBqajYgbAuWA2lm-uKMR4Ctc-I828IXrEkVf0BMo0w6QUpY_0HFvHqzdDYAbO5Z1d2W7pKiSGZYjEeVBGOLLiDs3tRahDY7izpLz_CmLt0CxTFaAmCCyxl8-AqRkeDvdWa0zsYo; _gat=1; UserMatchHistory=AQLyy7PpGI4lQwAAAW9c7EazSGHJYVJEmb73egPFKQ4IiteCb9CGSUo2QbhgQSUseQsgB2ypESB9gi1AqGNNAtClCAN4xLXa4erjDtRlYxPeL3W7gW01hCmrRTSRdQJydeBeXV8PxlQb9mp7Yqc3d_8hL73CO2dh_khzFoxlsqBrdx6Xp6hesKVyHzplKpH-uk-3mQ; lidc="b=SB78:g=130:u=77:i=1577812014:t=1577845538:s=AQGg8nJrb1D_eXRaE6gg89KD2V2KiodR"'
PAGINATION_TOKEN = '612001978-1577811980414-a8b14b6f297ef72b4d2dc687ebdc346b'

payload = {
        'csrf-token': CSRF_TOKEN,
        'user-agent': USER_AGENT,
        'cookie': FEED_COOKIE,
    }
import requests
import logging

# Creating Logger
logging.basicConfig(filename="one_pace_downloader.log", format='%(asctime)s %(message)s', encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger()
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_download_page():
    url = "https://onepace.net/watch"
    try:
        resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"})
        status = resp.status_code
        if status == 200:
            pass
        else:
            raise ConnectionError("Request failed")
    except ConnectionError as err:
        logger.info(err)
    else:
        return resp.text


def main():
    pass

if __name__ == '__main__':
    main()
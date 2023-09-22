import requests
import logging
from bs4 import BeautifulSoup

# Creating Logger
logging.basicConfig(filename="one_pace_downloader.log", format='%(asctime)s %(message)s', encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger()
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class Arc:
    def __init__(self, name, links):
        self.name = name
        self.episodes = self.get_magnet_links(links)

    def get_magnet_links(self, links):
        magnets = [link for link in links if 'magnet' in link]
        print(magnets)
        return magnets

    def __repr__(self):
        return self.name

class Page:
    def __init__(self):
        self.page = self.get_download_page()

    def get_download_page(self):
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
            bs = BeautifulSoup(resp.content, 'html.parser')
            return bs

    def get_arc(self, arc):
        name = None
        links = None
        try:
            for section in self.page.find_all('section', attrs={"class": "Carousel_root__t7h0u"}):
                if section.find('h2').text.lower() == arc:
                    name = section.find('h2').text
                    links = [a['href'] for a in section.find_all('div', href=True)]
                    break
            if not name or not links:
                raise TypeError("Failed to find Arc")
        except TypeError as err:
            logger.info(err)
        else:
            arc = Arc(name, links)
            return arc



def main():
    page = Page()


if __name__ == '__main__':
    main()
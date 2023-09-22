import unittest
import one_pace_downloader
from bs4 import BeautifulSoup

class TestOnePaceDownloader(unittest.TestCase):
    # test if get_download_page retreives the page
    def test_get_download_page(self):
        p = one_pace_downloader.Page()
        self.assertEqual(p.page.find('title').text, 'Watch One Pace | The Definitive One Piece Viewing Experience')

    def test_get_arc_by_title(self):
        arc = 'water seven'
        p = one_pace_downloader.Page()

        self.assertEqual((p.get_arc(arc)).name.lower(), "water seven")
    def test_if_arc_class_gets_magnet_links(self):
        arc = "water seven"
        p = one_pace_downloader.Page()

        arc = p.get_arc(arc)

        self.assertIsInstance(arc.episodes, list)

import unittest
import one_pace_downloader

class TestOnePaceDownloader(unittest.TestCase):
    # test if get_download_page retreives the page
    def test_get_download_page(self):
        self.assertIsInstance(one_pace_downloader.get_download_page(), str)
    def test_if_exception_is_raised_on_unsuccessful_reqeust(self):

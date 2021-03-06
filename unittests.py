import unittest
from main import geturls


class TestUrlParsing(unittest.TestCase):
    def test_google_block(self):
        self.assertEqual(geturls("google.com:443/search"), '"blocked"')

    def test_google_fail(self):
        self.assertRaises(BaseException, geturls, "google.uk:80/test_path")


if __name__ == '__main__':
    unittest.main()
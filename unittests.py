import unittest
from main import geturls


class TestUrlParsing(unittest.TestCase):
    def test_google_block(self):
        self.assertEqual(geturls("google.com/search"), '"blocked"')

    def test_google_fail(self):
        self.assertRaises(BaseException, geturls, "google.uk")


if __name__ == '__main__':
    unittest.main()
from unittest import TestCase
from picso import Album

class PicsoTestCase(TestCase):
    def setUp(self):
        self.album = Album()

    def tearDown(self):
        self.album = None

    def test_init(self):
        self.assertEqual(self.album.title,'New Album')
        self.assertEqual(self.album.size,0)
    def test_load(self):
        self.album.load('~/home/github/picso/tests/fixtures/data','.png')
        self.assertIn('file1.png', self.album.content)
        self.assertNotIn('file1.txt', self.album.content)
        self.assertEqual(self.album.size, 5)
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
        list_of_files = ['file1.png', 'file2.png', 'file3.png', 'file4.png', 'file5.png']
        list_of_scores = [1, 4, 2, 0, 3]
        self.album.load('~/home/github/picso/tests/fixtures/data','.png')
        self.assertEqual(np.array_equal(self.album.content.keys(), list_of_files), True)
        self.assertEqual(np.array_equal(self.album.content.values(), list_of_scores), True)
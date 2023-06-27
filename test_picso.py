import numpy as np
from unittest import TestCase
from picso import Album


class TestAlbum(TestCase):

    def setUp(self):
        self.album = Album(title='Test Album')

    def tearDown(self):
        self.album = None

    def test_init(self):
        self.assertEqual(self.album.title, 'Test Album')
        self.assertEqual(self.album.size, 0)

    def test_load(self):
        self.album.load(dir_path='fixtures/data', file_extension='.png')
        list_of_files = ['file1.png', 'file2.png', 'file3.png', 'file4.png', 'file5.png']
        list_of_scores = [1, 4, 2, 0, 3]
        self.assertEqual(np.array_equal(list(self.album.content.keys()), list_of_files), True)
        self.assertEqual(np.array_equal(list(self.album.content.values()), list_of_scores), True)
        self.assertRaises(TypeError, self.album.load(), title=0)
        self.assertRaises(TypeError, self.album.load(), file_extension=0)

    def test_random_pair(self):
        self.album.load(dir_path='fixtures/data', file_extension='.png')
        choice1 = self.album.random_pair()
        choice2 = self.album.random_pair()
        self.assertIn(choice1[0], self.album.content.keys())
        self.assertIn(choice1[1], self.album.content.keys())
        self.assertNotEqual(np.array_equal(choice1, choice2), True)

    def test_switch(self):
        self.album.load(dir_path='fixtures/data', file_extension='.png')
        self.album.switch('file1.png', 'file2.png')
        self.assertEqual(self.album.content['file1.png'], 4)
        self.assertEqual(self.album.content['file2.png'], 1)
        self.assertRaises(ValueError, self.album.switch, picture1='file1.png', picture2='test')
        self.assertRaises(ValueError, self.album.switch, picture1='test', picture2='file1.png')
        self.assertRaises(ValueError, self.album.switch, picture1='file1.png', picture2='file1.png')

from unittest import TestCase

import numpy as np

from picso import Album


class PicsoTestCase(TestCase):
    def setUp(self):
        self.album = Album(title='Test Album')

    def tearDown(self):
        self.album = None

    def test_init(self):
        self.assertEqual(self.album.title, 'Test Album')

    def test_load(self):
        # happy paths
        self.album.load('~/home/github/picso/tests/fixtures/data', '.png')
        list_of_files = ['file1.png', 'file2.png', 'file3.png', 'file4.png', 'file5.png']
        list_of_scores = [1, 4, 2, 0, 3]
        self.assertEqual(np.array_equal(self.album.content.keys(), list_of_files), True)
        self.assertEqual(np.array_equal(self.album.content.values(), list_of_scores), True)

        # errors
        self.assertRaises(TypeError, self.album.load(), title=0)
        self.assertRaises(TypeError, self.album.load(), file_extension=0)

    def test_random_pair(self):
        choice1 = self.album.random_pair()
        choice2 = self.album.random_pair()
        self.assertIn(choice1[0], self.album.content.keys())
        self.assertIn(choice1[1], self.album.content.keys())
        self.assertNotEqual(np.array_equal(choice1, choice2), True)

    def test_switch(self):
        # happy paths
        self.album.switch('file1.png', 'file2.png')
        self.assertEqual(self.album.content['file1.png'], 4)
        self.assertEqual(self.album.content['file2.png'], 1)

        # errors
        self.assertRaises(ValueError, self.album.switch(picture1='file1.png', picture2='test'))
        self.assertRaises(ValueError, self.album.switch(picture1='test', picture2='file1.png'))
        self.assertRaises(ValueError, self.album.switch(picture1='file1.png', picture2='file1.png'))

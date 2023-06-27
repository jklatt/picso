import os
import numpy as np


class Album:
    """Collection of pictures and respective scores"""

    def __init__(self, title='New Album'):
        """
        :type title: str
        """
        self.content = {}
        self.size = 0
        # check correctness of parameter types
        if type(title) != str:
            raise TypeError("title must be a string")
        else:
            self.title = title

    def __str__(self):
        return f"Album '{self.title}', {self.size} pictures"

    def load(self, dir_path='.', file_extension='.jpg'):
        """Loads all file names within a given directory and with a given extension into a dictionary
        :type dir_path: str
        :type file_extension: str
        """

        # check correctness of parameter types
        if type(dir_path) != str:
            raise TypeError("dir_path must be a string")
        if type(file_extension) != str:
            raise TypeError("file_extension must be a string")

        # obtain list of *.<file_extension> files in <dir_path>
        list_of_files = [file_name for file_name in os.listdir(dir_path) if file_name.endswith(file_extension)]
        list_of_files.sort()

        # create list of random integer scores between (including) 0 and number of pictures minus 1
        list_of_scores = np.random.RandomState(42).permutation(len(list_of_files))

        # populate the album dictionary and assign
        for name, score in zip(list_of_files, list_of_scores):
            self.content[name] = score

        # adjust the size of the album
        self.size = len(self.content)

    def random_pair(self):
        """Randomly selects two of the pictures in a dictionary"""

        return np.random.choice(list(self.content.keys()), size=2, replace=False)

    def switch(self, picture1, picture2):
        """Switches scores of two pictures
        :type picture1: str
        :type picture2: str
        """

        # check correctness of parameter types
        if type(picture1) != str:
            raise TypeError("picture1 must be a string")
        if type(picture2) != str:
            raise TypeError("picture2 must be a string")

        # check correctness of file names
        if picture1 not in self.content:
            raise ValueError("picture1 wasn't found in album content")
        if picture2 not in self.content:
            raise ValueError("picture2 wasn't found in album content")
        if picture1 == picture2:
            raise ValueError("picture1 must not be equal to picture2")

        # store scores
        score1 = self.content[picture1]
        score2 = self.content[picture2]

        # switch scores
        self.content[picture1] = score2
        self.content[picture2] = score1

#    def compare(self, picture1, picture2):
#        """Facilitates user-based comparison of two pictures
#        :type picture1: str
#        :type picture2: str
#        """
#
#        # check correctness of parameter types
#        if type(picture1) != str:
#            raise TypeError("picture1 must be a string")
#        if type(picture2) != str:
#            raise TypeError("picture2 must be a string")
#
#        # Prompt user to compare the two pictures
#        print(f"Do you prefer {picture1} (1) or {picture2} (2)?")
#
#        # Register the users preference
#        user_preference = input()
#
#        # Translate user preference into ordering of scores
#        if user_preference==1:
#            if self.content[picture1] < self.content[picture2]:

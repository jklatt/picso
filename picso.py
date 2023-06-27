class Album:
    """Collection of pictures and respective scores"""

    def __init__(self, title, size):
        self.title = title
        self.size = size

    def __str__(self):
        return f"Album '{self.title}', {self.size} pictures"


class Picture:
    """Picture and respective score"""

    def __init__(self, title, score):
        self.title = title
        self.score = score

    def __str__(self):
        return f"Picture '{self.title}', score {self.score} pictures"


def load(file_directory: str, file_extension: str):
    """Loads all file names within a given directory and with a given extension into a dictionary"""

    # check correctness of parameter types
    if type(file_directory) != str:
        raise TypeError("file_directory must be a string")
    if type(file_extension) != str:
        raise TypeError("file_extension must be a string")

    # create dictionary of pictures
    album = {}

    return album


def initialize(album: dict):
    """Randomly assigns a unique integer score to each of the pictures in a dictionary"""

    # check correctness of parameter types
    if type(album) != dict:
        raise TypeError("album must be a dictionary")

    return album


def select_pair(album: dict):
    """Randomly selects two of the pictures in a dictionary"""

    # check correctness of parameter types
    if type(album) != dict:
        raise TypeError("album must be a dictionary")

    picture1 = {}
    picture2 = {}

    return picture1, picture2


def compare(picture1: dict, picture2: dict):
    """Facilitates user-based comparison of two pictures"""

    # check correctness of parameter types
    if type(picture1) != dict:
        raise TypeError("picture1 must be a dictionary")
    if type(picture2) != dict:
        raise TypeError("picture2 must be a dictionary")

    return picture1, picture2


def switch(picture1: dict, picture2: dict):
    """Switches scores of two pictures"""

    # check correctness of parameter types
    if type(picture1) != dict:
        raise TypeError("picture1 must be a dictionary")
    if type(picture2) != dict:
        raise TypeError("picture2 must be a dictionary")

    return picture1, picture2

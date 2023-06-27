import numpy
def load(file_directory: str, file_extension: str):
    """Loads all file names within a given directory and with a given extension into a dictionary"""

    # check correctness of parameter types
    if type(file_directory) != str:
        raise TypeError("file_directory must be a string")
    if type(file_extension) != str:
        raise TypeError("file_extension must be a string")

    # create dictionary of objects
    dictionary_of_objects = {}

    return dictionary_of_objects

def initialize(dictionary_of_objects: dict):
    """Randomly assigns a unique integer score to each of the objects in a dictionary"""

    # check correctness of parameter types
    if type(dictionary_of_objects) != dict:
        raise TypeError("dictionary_of_objects must be a dictionary")

    return dictionary_of_objects

def select_pair(dictionary_of_objects: dict):
    """Randomly selects two of the objects in a dictionary"""

    # check correctness of parameter types
    if type(dictionary_of_objects) != dict:
        raise TypeError("dictionary_of_objects must be a dictionary")

    (object1, object2) = ()

    return (object1, object2)

def compare(object1: dict, object2: dict):
    """Facilitates user-based comparison of two objects"""

    # check correctness of parameter types
    if type(object1) != dict:
        raise TypeError("object1 must be a dictionary")
    if type(object2) != dict:
        raise TypeError("object2 must be a dictionary")

    return (object1, object2)

def switch(object1: dict, object2: dict):
    """Switches scores of two objects"""

    # check correctness of parameter types
    if type(object1) != dict:
        raise TypeError("object1 must be a dictionary")
    if type(object2) != dict:
        raise TypeError("object2 must be a dictionary")

    return (object1, object2)

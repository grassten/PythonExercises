import datetime

"""
This script creates an empty file.
"""

filename = datetime.datetime.now()


def create_file():
    """This function creates an empty file"""
    with open(filename.strftime("%B-%d-%Y") + ".txt", "w") as file:
        file.write("")  # writing empty string


create_file()

""" Purpose of script is to automate operations by first listing files in folder. """

import glob

def list_files():
    """ Function lists all the files with the .JPG file extension and displays the filename of the first and last file.
        Folder with photos lies relative to main.py in Data/photos outside of the venv.
    """

    # Test folder
    #list_of_photos: list[str] = glob.glob("photos/*.JPG")
    # Actual folder in Data
    list_of_photos: list[str] = glob.glob("../../../../Data/photos/*.JPG")
    print("File listing:")
    print(f"# of photos in folder: {len(list_of_photos)}")
    print(f"First photo in folder:  {list_of_photos[0]}")
    print(f"Last photo in folder:  {list_of_photos[ len(list_of_photos)-1 ]}")

    return list_of_photos

def list_files_dev():
    """ Function used for dev

    """

    list_of_photos_dev: list[str] = glob.glob("photos/*.JPG")

    return list_of_photos_dev

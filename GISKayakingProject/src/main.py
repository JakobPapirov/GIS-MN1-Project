# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from batch import list_files
from exif_worker import exif_qty_gps_data, exif_extract_gps_data

# Dev purposes
from batch import list_files_dev
from exif_worker import exif_read_folder_dev

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 1. Generate JPG file list
    list_of_photos = list_files()

    # 2. Determine exif properties of photos
    exif_qty_gps_data(list_of_photos)

    # 3. Extract exif gps data and export as csv
        # Foo 1 Extract data
        # Foo 2 Export to csv
    exif_extract_gps_data(list_of_photos)
    # The entire process took 9-10 s

    # Dev purposes
    #list_of_photos_dev = list_files_dev()

    #exif_read_folder_dev(list_of_photos_dev)

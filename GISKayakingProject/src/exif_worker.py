""" Script performs various tasks on photos. """

from exif import Image
import csv

from coords_dms_to_dec import coords_dms_to_dec as coords_conv

def exif_qty_gps_data(list_of_photos):
    """ Function determines the number of photos with exif data and GPS data."""

    qty_photos_exif_data = 0
    qty_photos_gps_data = 0

    for photo in list_of_photos:
        with open(photo, 'rb') as img_file:
            img = Image(img_file)

            img_status = img.has_exif
            if img_status == True:
                qty_photos_exif_data += 1

            # Assumption: if gps latitude is present then gps longitude should be as well
            if img.get('gps_latitude') is not None:
                qty_photos_gps_data += 1

    print("")
    print("Photos exif data:")
    print(f"# of photos with exif data: {qty_photos_exif_data}")
    print(f"# of photos with exif and GPS data: {qty_photos_gps_data}")
    print(
        f"Percent of photos with exif and gps data: {round((qty_photos_gps_data / len(list_of_photos)) * 100, ndigits=2)}")

def exif_extract_gps_data(list_of_photos):
    """ Docstring """

    print("")
    print("Extracting Exif GPS data...")

    data_to_export = []
    for photo in list_of_photos:

        data_row_to_export = []

        with open(photo, 'rb') as img_file:
            img = Image(img_file)

            if img.get('gps_latitude') is not None:
                # Image has exif GPS data. Assumption: if it has latitude data then it also has longitude data

                data_row_to_export.append(img.get('datetime_original'))

                coords_dec_lat = coords_conv(img.get('gps_latitude'))
                coords_dec_long = coords_conv(img.get('gps_longitude'))

                data_row_to_export.append(coords_dec_lat)
                data_row_to_export.append(coords_dec_long)
                data_row_to_export.append(img.get('gps_altitude'))

        data_to_export.append(data_row_to_export)

    exif_to_csv(data_to_export)
    print("Export successful")

def exif_set_exif_data(list_of_photos):
    """ Function receives a list of photos and sets exif data.
        Note function does not overwrite photos; exif_save_modified does that.
    """

    for photo in list_of_photos:
        with open(photo, 'rb') as img_file:
            img = Image(img_file)

            img.copyright = "Jakob Papirov"

            # exif_save_modified()


def exif_save_modified():
    pass


def exif_to_csv(exif_gps_data):
    """ docstring """

    print("")
    print("Exporting data to CSV ...")

    with open('photos_exif_gps_data_dec.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        for line in exif_gps_data:
            csv_writer.writerow(line)

# Used for dev purposes
def exif_read():
    """ Functions reads in an image and prints metadata """

    folder_path = "photos"
    img_filename = "2019-09-02_18.05.24.JPG"
    img_path = f"{folder_path}/{img_filename}"

    with open(img_path, 'rb') as img_file:
        img = Image(img_file)

    print("Checking if your image has any exif data...", img.has_exif)

    print("")
    print("Lists all available attributes")

    # print( sorted(img.list_all()) )
    available_attributes = sorted(img.list_all())
    for attribute in available_attributes:
        print(attribute)

    print("")
    print(f"DateTime (original): {img.get('datetime_original')}")
    print(f"GPS Lat: {img.get('gps_latitude')}")
    print(f"GPS Long: {img.get('gps_longitude')}")
    print(f"GPS Altitude: {img.get('gps_altitude')}")
    print(f"GPS Status: {img.get('gps_status')}")
    # print(f"GPS Altitude: {img.get('gps_altitude')}")

    print(f"Copyright: {img.get('copyright')}")
    img.copyright = "Jakob Papirov"
    print(f"Copyright: {img.get('copyright')}")

def exif_read_folder_dev(list_of_photos):
    """ docstring """

    print("Dev function running")
    qty_photos_exif_data = 0
    qty_photos_gps_data = 0

    for photo in list_of_photos:
        with open(photo, 'rb') as img_file:
            img = Image(img_file)

            img_status = img.has_exif
            if img_status == True:
                qty_photos_exif_data += 1

            if img.get('gps_latitude') is not None:
                qty_photos_gps_data += 1

            print("Checking if your image has any exif data...", img.has_exif)

            print("")
            print("Lists all available attributes")

            # available_attributes = sorted(img.list_all())
            # for attribute in available_attributes:
            #    print(attribute)

            # Turn this code into a separate function, if needed
            print("")
            print(f"DateTime (original): {img.get('datetime_original')}")
            print(f"GPS Lat: {img.get('gps_latitude')}")
            print(f"GPS Long: {img.get('gps_longitude')}")
            print(f"GPS Altitude: {img.get('gps_altitude')}")
            print(f"GPS Status: {img.get('gps_status')}")
            # print(f"GPS Altitude: {img.get('gps_altitude')}")

            print(f"Copyright: {img.get('copyright')}")

            coords_lat = img.get('gps_latitude')
            if coords_lat is not None:
                coords_lat = tuple(coords_lat)
                x, y, z = coords_lat
                print(f"Lat values {x}, {y}, {z}")

            # Save a copy of file
            # Errors
            # File "D:\Jakob\Dropbox\Studier\T05\04 GIS MN1\GIS VT 2020\Projekt\Kayak2019\Programming\Python\GISKayakingProject\src\exif_worker.py", line 78, in exif_read_folder
            # with open(f"mod_{img_file}", 'wb') as new_image_file:
            # OSError: [Errno 22] Invalid argument: "mod_<_io.BufferedReader name='photos\\\\2019-09-02_15.55.39.JPG'>"
        # Works when not specifying a prefix

        # with open(f"{photo}", 'wb') as new_image_file:
        #    new_image_file.write(img.get_file())
        #print(f"Type {type(coords_lat)}")


""" docstring """

from exif import Image

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

    #print( sorted(img.list_all()) )
    available_attributes = sorted(img.list_all())
    for attribute in available_attributes:
        print(attribute)

    print("")
    print(f"DateTime (original): {img.get('datetime_original')}")
    print(f"GPS Lat: {img.get('gps_latitude')}")
    print(f"GPS Long: {img.get('gps_longitude')}")
    print(f"GPS Altitude: {img.get('gps_altitude')}")
    print(f"GPS Status: {img.get('gps_status')}")
    #print(f"GPS Altitude: {img.get('gps_altitude')}")

    print(f"Copyright: {img.get('copyright')}")
    img.copyright = "Jakob Papirov"
    print(f"Copyright: {img.get('copyright')}")

def exif_read_folder(list_of_photos):
    """ docstring """

    qty_photos_exif_data = 0
    qty_photos_gps_data = 0

    for photo in list_of_photos:
        with open(photo, 'rb') as img_file:
            img = Image(img_file)

            img_status = img.has_exif
            if img_status == True:
                qty_photos_exif_data += 1

            if img.get('gps_latitude') != None:
                qty_photos_gps_data += 1

            print("Checking if your image has any exif data...", img.has_exif)

            print("")
            print("Lists all available attributes")

            #available_attributes = sorted(img.list_all())
            #for attribute in available_attributes:
            #    print(attribute)

            # Turn this code into a separate function, if needed
            print("")
            print(f"DateTime (original): {img.get('datetime_original')}")
            print(f"GPS Lat: {img.get('gps_latitude')}")
            print(f"GPS Long: {img.get('gps_longitude')}")
            print(f"GPS Altitude: {img.get('gps_altitude')}")
            print(f"GPS Status: {img.get('gps_status')}")
            # print(f"GPS Altitude: {img.get('gps_altitude')}")

            # Split this up into function
            # Set exit data
            img.copyright = "Jakob Papirov"
            print(f"Copyright: {img.get('copyright')}")

            # Save a copy of file
                # Errors
                #File "D:\Jakob\Dropbox\Studier\T05\04 GIS MN1\GIS VT 2020\Projekt\Kayak2019\Programming\Python\GISKayakingProject\src\exif_test.py", line 78, in exif_read_folder
                #with open(f"mod_{img_file}", 'wb') as new_image_file:
                #OSError: [Errno 22] Invalid argument: "mod_<_io.BufferedReader name='photos\\\\2019-09-02_15.55.39.JPG'>"
        with open(f"{photo}", 'wb') as new_image_file:
            new_image_file.write(img.get_file())

    print(qty_photos_exif_data)
    print(qty_photos_gps_data)
    print(f"Percent of photos with exif gps data: { round((qty_photos_gps_data/len(list_of_photos))*100, ndigits=2)}")


def exif_save_modified():
    pass

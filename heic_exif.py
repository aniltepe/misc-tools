import io
import pyheif
import PIL
import exifread

def read_heic(path: str):
    with open(path, 'rb') as file:
        image = pyheif.read_heif(file)
        for metadata in image.metadata or []:
            if metadata['type'] == 'Exif':
                fstream = io.BytesIO(metadata['data'][6:])
    tags = exifread.process_file(fstream)
    new_file = open(FILE_DIRECTORY + FILE_NAME.split(".")[0] + "_exif.txt", "w+")
    new_line = ""
    for tag in tags.keys():
        new_line += "Key: %s, value %s\n" % (tag, tags[tag])
    new_file.write(new_line[:-1])
    new_file.close()
    
FILE_DIRECTORY = "/Users/nazimaniltepe/Downloads/"
FILE_NAME = "IMG_0933.HEIC"

read_heic(FILE_DIRECTORY + FILE_NAME)
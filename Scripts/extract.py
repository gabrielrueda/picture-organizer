import os
from datetime import date
from PIL import Image
from PIL.ExifTags import TAGS

directories = list()
files = list()

def fileNames(path):
    return os.listdir(path)

# def folderNames(path):
#     for item in os.listdir(path):
#         if(os.path.isdir(path + "/" + item)):
#             directories.append(item)
#     return directories

def currentYear():
    today = date.today()
    return int(today.strftime("%Y"))

def getDate(imagename):
    try:
        image = Image.open(imagename)
        exifdata = image.getexif()
        # Opens data and finds the date
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id) 
            if isinstance(data, bytes):
                data = data.decode()
            if(tag == "DateTime"):
                return [data[0:4],data[5:7],data[8:10]]
    except IOError:
        return None




import os
import shutil
import extract
import random

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def createFolders(nameData, path):
    # Turns nameData into a 1d list
    tempData = sum(nameData, [])
    year = 1000
    while(year <= extract.currentYear()):
        if(tempData.count(str(year)) > 0):
            os.mkdir(path + "/" + str(year))
        year += 1
    for sect in nameData: 
        try:
            os.mkdir(path + "/" + sect[0] + "/" + months[(int(sect[1]) - 1)])
        except FileExistsError:
            pass

def relocate(path):
    for (root,dirs,files) in os.walk(path, topdown=True): 
        print(root)
        if(root != path):
            for f in files:
                while True:
                    try:
                        shutil.move(root + "/" + f, path)
                        break
                    except shutil.Error as err:
                        before = f
                        ext = os.path.splitext(f)[1]
                        f = str(random.randint(1,10000000000000)) + ext
                        os.rename(root + "/" + before, root + "/" + f)

def deleteDirectories(path):
    everything = os.listdir(path)
    for f in everything:
        if(os.path.isdir(path + "/" + f)):
            shutil.rmtree(path + "/" + f)

def moveToMisc(filename, path):
    try:
        os.mkdir(path + "/Misc")
    except:
        pass
    shutil.move(filename, path + "/Misc")

def moveFiles(nameData, path):
    for name in nameData:
        if(name[3] > 1):
            shutil.move(path + "/" + name[0] + "-" + name[1] + "-" + name[2] + " (" + str(name[3]-1) + ")" + ".jpg", path + "/" + name[0] + "/" + months[(int(name[1]) - 1)])
        else:
            shutil.move(path + "/" + name[0] + "-" + name[1] + "-" + name[2] + ".jpg", path + "/" + name[0] + "/" + months[(int(name[1]) - 1)])

# def deleteSubFolders(path):
#     print(os.listdir(path))
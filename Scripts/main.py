import os
import shutil
import extract
import move
from pathlib import Path


# Path to folder
nameData = list()

def rename(imagename, path, date, extraNum):
    additionalString = ""
    eNum = extraNum
    while True:
        try:
            os.rename(imagename, path + "/" + date[0] + "-" + date[1] + "-" + date[2] + additionalString + ".jpg")
            break
        except FileExistsError:
            additionalString = " (" + str(eNum) + ")"
            eNum += 1
    return eNum

def backup(path):
    move.relocateToPicturesFolders(path)
    # os.mkdir(path + "/Backup")
    shutil.copytree(path + "/Pictures", path + "/Backup")

def mainFunction():
    print("This program is designed to organize your pictures in the date they were taken.")
    path = input("Write the path to the folder you wish to organize:")
    backup(path)
    path = path + "/Pictures"
    print("Moving files and deleting old subdirectories...")
    move.relocate(path)
    move.deleteDirectories(path)
    print("Renaming pictures...")
    files = extract.fileNames(path)
    for i in files:
        extraNum = 1
        imagename = path + "/" + i
        date = extract.getDate(imagename)
        if(date == None):
            move.moveToMisc(imagename, path)
        else:
            extraNum = rename(imagename, path, date, extraNum)
            date.append(extraNum)
            nameData.append(date)
    print("Creating new folders...")
    move.createFolders(nameData, path)
    print("Moving pictures to their corresponding folders....")
    move.moveFiles(nameData, path)
    deleteBackup = input("Would you like to delete your backup?")
    print("Complete.")

mainFunction()

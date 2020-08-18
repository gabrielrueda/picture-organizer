import os
import extract
import move


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

def mainFunction():
    print("This program is designed to organize your pictures in the date they were taken.")
    path = input("Write the path to the folder you wish to organize:")
    move.relocate(path)
    move.deleteDirectories(path)
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

    move.createFolders(nameData, path)
    move.moveFiles(nameData, path)

mainFunction()

#  =================================================
#  |                  FileManager                  |
#  |                    ancymon                    |
#  =================================================

from os import listdir
import os
from os.path import isfile, join

os.system("Color A")
version = "1.0.0"


# Feel free to change it ;)
def branding():
    os.system("title FileManager v"+version+" by ancymon")
    print("=================================================",
          "|                  FileManager                  |",
          "|                    ancymon                    |",
          "=================================================",
          sep="\n", end="\n\n")


def selectPath():
    os.system("cls")
    branding()
    print("Path: ", end="")
    path = input("")
    try:
        [f for f in listdir(path) if isfile(join(path, f))]
    except:
        input("Error while loading the path '" +
              path+"'\nPress ENTER to continue...")
        selectPath()
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(path, end="\n  ")
    print("\n  ".join(onlyfiles))
    if input("Is this the right path? [y/n] ") != "y":
        selectPath()
    else:
        selectMode(onlyfiles, path)


def selectMode(onlyfiles, path):
    os.system("cls")
    branding()
    print("Path: "+path)
    print("Select mode:", "   1. Add prefix to every file", "   > 'file.txt', 'secondfile.exe' => 'prefix_file.txt', 'prefix_secondfile.txt'",
          "", "   2. Rename all files", "   > 'file.txt', 'secondfile.exe' => 'input1.txt','input2.exe'", "", "   3. Delete all files from directory", "   > 'file.txt', 'secondfile.exe' => '', ''", sep="\n", end="\nMode: ")
    mode = input()
    if mode in ["1", "2", "3"]:
        os.system("cls")
        branding()
        print("Path: "+path, "Select mode: "+mode, sep="\n")
        if mode == "1":
            prefix = input("Select prefix: ")
            fnum = 0
            for f in onlyfiles:
                fnum += 1
                print("Changing "+str(len(onlyfiles))+" file names ("+str(int(100*(fnum /
                      len(onlyfiles))))+"%)", end="\r")
                if f != os.path.basename(__file__):
                    os.rename(path+"\\"+f, path+"\\"+prefix+f)
            print("\nSuccessfully added prefixes\nPress ENTER to continue...")
            input()
            selectPath()
        elif mode == "2":
            newname = input("Select new file name: ")
            fnum = 0
            for f in onlyfiles:
                fnum += 1
                ext = f.split(".")
                fnewname = ""
                for i in range(len(ext)):
                    if i == 0:
                        fnewname += newname+str(fnum)
                    else:
                        fnewname += "."+ext[i]
                print("Changing "+str(len(onlyfiles))+" file names ("+str(int(100*(fnum /
                                                                                   len(onlyfiles))))+"%)", end="\r")
                if f != os.path.basename(__file__):
                    os.rename(path+"\\"+f, path+"\\"+fnewname)
            print("\nSuccessfully added prefixes\nPress ENTER to continue...")
            input()
            selectPath()
        elif mode == "3":
            delete = input(
                "Are you sure? This proccess will delete all of the files in '"+path+"' [y/n] ")
            if delete == "y":
                os.system("cls")
                branding()
                print("Path: "+path, "Select mode: "+mode,
                      "Confirmation: "+delete, sep="\n")
                fnum = 0
                for f in onlyfiles:
                    fnum += 1
                    print("Deleting "+str(len(onlyfiles))+" files ("+str(int(100*(fnum /
                          len(onlyfiles))))+"%)", end="\r")
                    if f != os.path.basename(__file__):
                        os.remove(path+"\\"+f)
                print("\nSuccessfully deleted "+str(len(onlyfiles)) +
                      " files\nPress ENTER to continue...")
                input()
                selectPath()
        else:
            selectPath()
    else:
        selectMode(onlyfiles, path)


selectPath()

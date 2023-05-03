#  =================================================
#  |                  FileManager                  |
#  |                    ancymon                    |
#  =================================================

from os import listdir
import os
from os.path import isfile, join

os.system("Color A")
version = "1.0.1"


# Feel free to change it ;)
brand = "=================================================\n|                  FileManager                  |\n|                    ancymon                    |\n=================================================\n"


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
        return selectPath()
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    print(path, end="\n  ")
    print("\n  ".join(onlyfiles))
    if input("Is this the right path? [y/n] ") != "y":
        return selectPath()
    else:
        selectMode(onlyfiles, path)


def selectMode(onlyfiles, path):
    os.system("cls")
    branding()
    print("Path: "+path)
    print("Select mode:", "   1. Add prefix to every file", "   > 'file.txt', 'secondfile.exe' => 'prefix_file.txt', 'prefix_secondfile.txt'",
          "", "   2. Rename all files", "   > 'file.txt', 'secondfile.exe' => 'input1.txt','input2.exe'", "", "   3. Change specified text in filename", "   > 'file.txt', 'secondfile.exe' => 'fchange.txt','secondfchange.exe'", "", "   4. Delete all files from directory", "   > 'file.txt', 'secondfile.exe' => '', ''", "", "   5. Fileflood", "   > '', '' => 'file1.flood.txt', 'file2.flood.txt'", sep="\n", end="\nMode: ")
    mode = input()
    if mode in ["1", "2", "3", "4", "5"]:
        os.system("cls")
        branding()
        print("Path: "+path, "Select mode: "+mode, sep="\n")
        if mode == "1":
            prefix = input("Select prefix: ")
            fnum = 0
            for f in onlyfiles:
                fnum += 1
                print("Changing "+str(len(onlyfiles))+" filenames ("+str(int(100*(fnum /
                      len(onlyfiles))))+"%)", end="\r")
                if f != os.path.basename(__file__):
                    os.rename(path+"\\"+f, path+"\\"+prefix+f)
            print("\n\nSuccessfully added prefixes\nPress ENTER to continue...")
            input()
            return selectPath()
        elif mode == "2":
            newname = input("Select new filename: ")
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
                print("Changing "+str(len(onlyfiles))+" filenames ("+str(int(100*(fnum /
                                                                                  len(onlyfiles))))+"%)", end="\r")
                if f != os.path.basename(__file__):
                    os.rename(path+"\\"+f, path+"\\"+fnewname)
            print("\n\nSuccessfully added prefixes\nPress ENTER to continue...")
            input()
            return selectPath()
        elif mode == "3":
            cFrom = input("From: ")
            cTo = input("To: ")
            fnum = 0
            for f in onlyfiles:
                fnum += 1
                ext = f.split(".")
                fnewname = ""
                for i in range(len(ext)):
                    if i == 0:
                        fnewname += ext[i].replace(cFrom, cTo)
                    else:
                        fnewname += "."+ext[i]
                print("Changing "+str(len(onlyfiles))+" filenames ("+str(int(100*(fnum /
                                                                                  len(onlyfiles))))+"%)", end="\r")
                if f != os.path.basename(__file__):
                    try:
                        os.rename(path+"\\"+f, path+"\\"+fnewname)
                    except:
                        continue
            print("\n\nSuccessfully changed filenames\nPress ENTER to continue...")
            input()
            return selectPath()
        elif mode == "4":
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
                print("\n\nSuccessfully deleted "+str(len(onlyfiles)) +
                      " files\nPress ENTER to continue...")
                input()
                return selectPath()
        elif mode == "5":
            flood = input("Number of files: ")
            try:
                flood = int(flood)
            except:
                input("Integer expected\nPress ENTER to continue...")
                return selectPath()
            flood = int(flood)
            for i in range(flood):
                print("Creating "+str(flood)+" files ("+str(int(100*((i+1) /
                                                                     flood)))+"%)", end="\r")
                try:
                    with open(path+"\\file"+str(i+1)+".flood.txt", 'w') as f:
                        f.write(
                            brand + "\nThis text file was generated using FileManager made by ancymon.\n> https://github.ancymon.lol\n\nThanks for using FileManager :D\n~ ancymon")
                except:
                    continue
            print("\n\nSuccessfully created "+str(flood) +
                  " files\nPress ENTER to continue...")
            input()
            return selectPath()
        else:
            return selectPath()
    else:
        selectMode(onlyfiles, path)


selectPath()

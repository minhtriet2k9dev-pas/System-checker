import os
import sys
from colorama import Fore, init, Style


init()


def warning(msg):
    print(Fore.YELLOW + "[!] WARNING: " + Style.RESET_ALL + msg)


def info(msg):
    print(Fore.BLUE + "[i] INFO: " + Style.RESET_ALL + msg)


def error(msg):
    print(Fore.RED + "[x] ERROR: " + Style.RESET_ALL + msg)


def success(msg):
    print(Fore.GREEN + "[+] SUCCESS: " + Style.RESET_ALL + msg)


home = os.path.expanduser("~")
folderpath = 'C:\\'
size = 0
listfile = []
filecount = 0
subfoldercount = 0
iserror = 0
f = open('errors.log', "w")

info("Start scanning folder \""+folderpath+'\"...')

for path, dirs, files in os.walk(folderpath):
    for f in files:
        fp = os.path.join(path, f)
        if os.path.isfile(fp):
            size += os.path.getsize(fp)
            listfile.append(fp)
            filecount += 1
            if filecount % 9 == 0:
                print(">      Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 1:
                print(">>     Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 2:
                print(">>>    Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 3:
                print(">>>>>  Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 4:
                print(">>>>>> Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 5:
                print(">>>>>  Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 6:
                print(">>>    Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
            if filecount % 9 == 8:
                print(">>     Scanning "+str(filecount) + " files, " +
                      str(subfoldercount)+' subfolders', end='\r')
        else:
            warning("Something goes wrong with FileIO system")
            error("cannot get File: \"" + fp + '\" size')
            f = open('errors.log', 'a')
            f.write("Cannot get File: \"" + fp + '\" size' + '\n')
            f.write("Reason: FileIO system cannot detect this path is a file\n")
            f.close()
            info("Skipping file: " + fp)
            iserror += 1
        # listfile.append(fp)
    for d in dirs:
        subfoldercount += 1

print(">>>>>> Scanning "+str(filecount) + " files")


def printinfo():
    print("Folder size   :  " + str(size) + ' bytes')
    print("                 " + str(size/1024) + ' KB')
    print("                 " + str(size/1024/1024) + ' MB')
    print("                 " + str(size/1024/1024/1024) + ' GB')
    print("="*40)
    print("Folder include : " + str(filecount) + ' files')
    print("                 " + str(subfoldercount) + ' subfolders')


if iserror:
    warning("There are some errors: " + str(iserror) + " files are skipped")
    warning("The info may not be correct")
    info("See errors.log file for more...")
    error("Cannot get all info from folder: \"" + folderpath + '\"')
else:
    success("Successfully get folder info: \"" + folderpath + '\"')
    print("")
    printinfo()

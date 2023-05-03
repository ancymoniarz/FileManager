# FileManager
Really simple file manager designed for quick file renaming and deleting
## How to use
### Find the directory that you want to commit changes to (ex. `C:\Users\user\Downloads\files`)
```
=================================================
|                  FileManager                  |
|                    ancymon                    |
=================================================

Path: C:\Users\user\Downloads\files
```
### Confirming chosen directory
```
=================================================
|                  FileManager                  |
|                    ancymon                    |
=================================================

Path: C:\Users\user\Downloads\files 
C:\Users\user\Downloads\files
  100percent-not-a-virus.exe
  normal-text-file.txt
  why-are-you-even-reading-the-file-names.txt
Is this the right path? [y/n] y
```
### Choosing mode
```
=================================================
|                  FileManager                  |
|                    ancymon                    |
=================================================

Path: C:\Users\user\Downloads\files
Select mode:
   1. Add prefix to every file
   > 'file.txt', 'secondfile.exe' => 'prefix_file.txt', 'prefix_secondfile.txt'

   2. Rename all files
   > 'file.txt', 'secondfile.exe' => 'input1.txt','input2.exe'

   3. Delete all files from directory
   > 'file.txt', 'secondfile.exe' => '', ''
Mode:
```
### Mode 1
```
=================================================
|                  FileManager                  |
|                    ancymon                    |
=================================================

Path: C:\Users\user\Downloads\files
Select mode: 1
Select prefix: myprefix_ 
```
### Mode 2
```
=================================================
|                  FileManager                  |
|                    ancymon                    |
=================================================

Path: C:\Users\user\Downloads\files
Select mode: 2
Select new file name: file
```
### Mode 3
```
=================================================
|                  FileManager                  |
|                    ancymon                    |
=================================================

Path: C:\Users\user\Downloads\files
Select mode: 3
Are you sure? This proccess will delete all of the files in 'C:\Users\user\Downloads\files' [y/n] y
```

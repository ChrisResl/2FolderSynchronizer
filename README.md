# 2FolderSynchronizer

## A program for synchronizing two folders

This synchronization tool maintains an identical copy of a source folder in a replica folder. The synchronization is one-way and periodic, and file creation, copying, and removal operations are logged to both a file and console output. The folder paths, synchronization interval, and log file path can be provided using command line arguments. 

## How to run

```
python 2FolderSynchronizer.py -s <directory_path> -r <directory_path> -l <output_path> -i <integer>
```

Example:
```
/home/chris/Workspace/2FolderSynchronizer/venv/bin/python /home/chris/Workspace/2FolderSynchronizer/src/2FolderSynchronizer.py -s ./testing/testing_directories/source -r ./testing/testing_directories/replica -l ./log.txt -i 10 

```

### Command line arguments
```
Input:
  -s or --source            Path of source folder
  -r or --replica           Path of replica folder

Synchronization:
  -i or --interval          Synchronization interval

Output:
  -l or --log               Path of log output file
```

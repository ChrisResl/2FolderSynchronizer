# 2FolderSynchronizer

## A program for synchronizing two folders

This synchronization tool maintains an identical copy of a source folder in a replica folder. The synchronization is one-way and periodic, and file creation, copying, and removal operations are logged to both a file and console output. The folder paths, synchronization interval, and log file path can be provided using command line arguments. 

## Command line arguments
```
Input:
  -s or --source            Path of source folder
  -r or --replica           Path of replica folder

Synchronization:
  -i or --interval          Synchronization interval

Output:
  -l or --log               Path of log output file
```

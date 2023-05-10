import os
import shutil
import datetime
import time


def write_to_log(log, message):
    """Writing a message to log output file
    :param log: string of path to log file
    :param message: string
    """
    with open(log, "a+") as f:
        f.write(message)
        f.close()


def deletion(source, replica, log):
    """Deleting directories and files in replica directory
    :param source: string of path to source directory
    :param replica: string of path to replica directory
    :param log: string of path to log file
    """
    source_structure = dict.fromkeys(os.listdir(source))
    replica_structure = dict.fromkeys(os.listdir(replica))

    for rel_path in replica_structure:
        if rel_path not in source_structure:
            abs_path = os.path.join(replica, rel_path)
            if os.path.isdir(abs_path):
                shutil.rmtree(abs_path)
                print("Directory " + rel_path + " was deleted")
                write_to_log(log, "Directory " + rel_path + " was deleted\n")
            else:
                os.remove(abs_path)
                print("File " + rel_path + " was deleted")
                write_to_log(log, "File " + rel_path + " was deleted\n")


def backup(source, replica, log):
    """Copying and creating files and directories in replica directory
    :param source: string of path to source directory
    :param replica: string of path to replica directory
    :param log: string of path to log file
    """
    source_structure = dict.fromkeys(os.listdir(source))
    replica_structure = dict.fromkeys(os.listdir(replica))

    if len(source_structure) == 0:
        return
    else:
        for rel_path in source_structure:
            abs_path_source = os.path.join(source, rel_path)
            abs_path_replica = os.path.join(replica, rel_path)

            # in case file/directory is only present in source
            if rel_path not in replica_structure:
                if os.path.isfile(abs_path_source):
                    shutil.copy2(abs_path_source, abs_path_replica)
                    print("File " + rel_path + " was created")
                    write_to_log(log, "File " + rel_path + " was created\n")
                else:
                    os.makedirs(abs_path_replica)
                    print("Directory " + rel_path + " was created")
                    write_to_log(log, "Directory " + rel_path + " was created\n")
                    backup(abs_path_source, abs_path_replica, log)
            # in case file/directory is present in both
            else:
                if os.path.isfile(abs_path_source):
                    shutil.copy2(abs_path_source, abs_path_replica)
                    print("File " + rel_path + " was copied")
                    write_to_log(log, "File " + rel_path + " was copied\n")
                else:
                    print("Directory " + rel_path + " was copied")
                    write_to_log(log, "Directory " + rel_path + " was copied\n")
                    backup(abs_path_source, abs_path_replica, log)


def synchronization(source, replica, interval, log):
    """Performing backup of source directory to replica directory
    :param source: string of path to source directory
    :param replica: string of path to replica directory
    :param interval: integer of interval seconds for repeating syncro
    :param log: string of path to log file
    """
    while True:
        write_to_log(log, "Synchronization between folder " + source + " and folder " + replica +
                     " performed at " + str(datetime.datetime.now()) + "\n")
        print("Synchronization between folder " + source + " and folder " + replica + " performed at "
              + str(datetime.datetime.now()) + "\n")
        # deleting files in replica
        deletion(source, replica, log)
        # creating and copying (to) files/directories in replica
        backup(source, replica, log)

        print()
        time.sleep(interval)

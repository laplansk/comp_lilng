import sys
import mail_utils
import os
import io
import shutil

rootdir = "./mail_data/all_labeled_messages"
for subdir, dirs, files in os.walk(rootdir):
    numFilesToProcess = 2000
    numTrueFound = 0
    for my_file in files:
        if numTrueFound >= numFilesToProcess:
            break
        try:
            with io.open(os.path.join(subdir, my_file), 'r', encoding='utf-8') as f:
                try:
                    for line in f:
                        # get True class value files (always first line of file)
                        if "True" in line:
                            shutil.copyfile(os.path.join(subdir, my_file), os.path.join(subdir, "../.././mail_data/true_messages/" + str(numTrueFound) + ".txt"))
                            numTrueFound += 1
                except UnicodeDecodeError as e:
                    print e
                    continue;
        except OSError:
            print("File not found")

        # print "processed fileNo: " + str(fileNo)

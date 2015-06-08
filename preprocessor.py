# This file takes in a .mbox file and outputs a text file for each message in the collection
# Each text file will have a Boolean on the first line, followed by all the plaintext from the message
# starting on the next line
# Example:
# True
# This is a message about X topic from Y person to Z person.

import sys
import mailbox
import mail_utils
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python preprocessor.py [mbox file]')
        sys.exit(1)

# df_name = "mail_data/training_data.mail"
# unlikely_string = "#!#!#!#!\n"

# check that command line arg is valid filepath
mboxfile = sys.argv[1]
if not os.path.isfile(mboxfile):
    print('Invalid filepath - exiting')
    sys.exit(1)

data_map = mail_utils.loadFile(mboxfile)

i = 0
for entry in data_map:
    destFile = open('./mail_data/test/' + str(i) + '.txt', 'w+')
    destFile.write(str(data_map[entry][1]) + '\n')
    destFile.write(data_map[entry][0])
    destFile.close()
    i += 1
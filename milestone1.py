import sys
import mailbox
import mail_utils
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)


data_file = sys.argv[1]
unlikely_string = "#!#!#!#!\n"

# read in data_file
def readData(filename, data_map):
    print "opening data file"
    # check that command line arg is valid filepath
    if not os.path.isfile(data_file):
        print('Invalid filepath - exiting')
        return False

    src = open(data_file, "r")
    input_number = 0
    while True:
        print "Message " + str(input_number)
        # walk until delimiter is read
        chunk = ""
        attachment_value = False
        while chunk != unlikely_string:
            chunk += src.read(1)
            if chunk == "":
                print "reached end of file"
                break

        # read Attachment boolean
        # if src.read(1) == "Y\n":
        print src.read(1)
            #attachment_value = True

        # read in message text
        body = ""
        while not unlikely_string in body:
            if input_number == 252:
                print "second inner"
            body += src.read(1)

        # cut off the unlikely_string
        body = body[:-len(unlikely_string)]

        data_map[input_number] = (body, attachment_value)
        input_number += 1




    print "closing data file"
    src.close()

data_map = {}
readData(data_file, data_map)






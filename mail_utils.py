import re
import mailbox
from threading import Thread

def hasAttachment(msg):
    pattern = re.compile('application/*')
    if msg.is_multipart():
        for part in msg.walk():
            if re.search(pattern, part.get_content_type()) is not None:
                return True
    elif re.search(pattern, msg.get_content_type()) is not None:
        return True
    else:
        return False


# This function returns true if the msg parameter has body text
def hasBody(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return True
    elif msg.get_content_type() == "text/plain":
        return True
    else:
        return False

# this function prints all first-level components of the msg parameter separated by newlines
def displayMessageComponents(msg):
    if msg.is_multipart():
        print "Multi:"
        for part in msg.walk():
            print "\t" + part.get_content_type()
            # print part.get_payload()
            # print ""
    else:
        print "Simple:"
        print msg.get_content_type()

# returns any plain text from msg. If email was void f p
def getPlainText(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                return part.get_payload()
    else:
        if msg.get_content_type() == "text/plain":
            return msg.get_payload()

# this function returns the subject of the msg parameter
def displaySubject(msg):
    return msg['subject']

# this function loads the data_map parameter with the message texts from the mboxfile parameter and
# whether or not the email has an attachment
#  _________________________________
# |______key______|______value______|
# |               |                 |
# |  email body   |   true/false    |
# |_______________|_________________|

def loadFile(mboxfile):
    data_map = {}
    print("loading, please wait")
    msg_num = 1
    for msg in mailbox.mbox(mboxfile):
        if msg_num % 1000 == 0:
            print("processed " + str(msg_num) + " messages")
        if not hasBody(msg):
            continue

        # YES or NO for having attachment
        has_attachment = False
        if hasAttachment(msg):
            has_attachment = True

        # write out the body of the email
        body = getPlainText(msg)
        data_map[msg_num] = (body, has_attachment)

        msg_num += 1

    print "load complete"
    return data_map

def loadGrams(gramfile):
    print("loading grams, please wait")
    with open(gramfile) as f:
        lines = f.readlines()

    # strip newlines
    for i in range(0, len(lines)):
        lines[i] = lines[i].rstrip("\n")

    return lines

def printMap(map):
    for item in map:
        print str(item) + " : " + str(map[item][1])
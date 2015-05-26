import re

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
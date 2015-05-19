import mailbox
import re

def displayMessageComponents(msg):
    for part in msg.walk():
        print part.get_content_type()

# This function returns true if the msg parameter has an attachment of the type application/*
def hasAttachment(msg):
    for part in msg.walk():
        pattern = re.compile('application/*')
        if re.search(pattern, part.get_content_type()) is not None:
            return part.get_content_type()

# this function returns the plain text message of an email if such text exists.
# If the email was empty, it returns the empty string
def getPlainTextBody(msg):
    for part in msg.walk():
        pattern = re.compile('text/plain')
        if re.search(pattern, part.get_content_type()) is not None:
            return part.get_payload()

# this function prints all first-level components of the msg parameter separated by newlines
def displayMessageComponents(msg):
    for part in msg.walk():
        print part.get_content_type()

# this function returns the subject of the msg parameter
def displaySubject(msg):
    return msg['subject']
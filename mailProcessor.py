import sys
import mailbox
import mail_utils
import os.path


#mboxfile = '../mail_data/smallFile0.mbox'
mboxfile = sys.argv[1]

# check that command line arg is valid filepath
if not os.path.isfile(mboxfile):
    print('Invalid filepath - exiting')
    sys.exit(1)

print(mboxfile)
messageNum = 1
payload = None

for msg in mailbox.mbox(mboxfile):
    if mail_utils.hasAttachment(msg) is not None:
        print "message " + str(messageNum) + " with attachment\n"
        messageNum += 1
        print "Subject: " + mail_utils.displaySubject(msg) + "\n"
        if mail_utils.getPlainTextBody(msg) is None:
            print "Body:\n EMPTY MESSAGE BODY\n"
        else:
            print "Body:\n" + mail_utils.getPlainTextBody(msg) + "\n"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)
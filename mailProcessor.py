import mailbox
import mail_utils

mboxfile = '../mail_data/smallFile0.mbox'

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

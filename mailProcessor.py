import sys
import mailbox
import mail_utils
import os.path

df_name = "mail_data/training_data.mail"
mboxfile = sys.argv[1]
unlikely_string = "#!#!#!#!\n"
# check that command line arg is valid filepath
if not os.path.isfile(mboxfile):
    print('Invalid filepath - exiting')
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)

print(mboxfile)
dest = open(df_name, "a")


i = 1
for msg in mailbox.mbox(mboxfile):
    print "processing message " + str(i)
    dest.write(unlikely_string)
    if not mail_utils.hasBody(msg):
        continue

    # YES or NO for having attachment
    if mail_utils.hasAttachment(msg):
        dest.write("YES\n")
    else:
        dest.write("NO\n")

    # write out the body of the email
    dest.write(mail_utils.getPlainText(msg) + "\n")
    i += 1

dest.close()






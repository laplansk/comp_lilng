import sys
import mailbox
import mail_utils
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)

df_name = "mail_data/training_data.mail"
mboxfile = sys.argv[1]
unlikely_string = "#!#!#!#!\n"
# check that command line arg is valid filepath
if not os.path.isfile(mboxfile):
    print('Invalid filepath - exiting')
    sys.exit(1)

print(mboxfile)
# dest = open(df_name, "a")


# i = 1
# for msg in mailbox.mbox(mboxfile):
#     print "processing message " + str(i)
#     dest.write(unlikely_string)
#     if not mail_utils.hasBody(msg):
#         continue
#
#     # YES or NO for having attachment
#     if mail_utils.hasAttachment(msg):
#         dest.write("Y\n")
#     else:
#         dest.write("N\n")
#
#     # write out the body of the email
#     dest.write(mail_utils.getPlainText(msg) + "\n")
#     dest.write(unlikely_string)
#     i += 1
#
# dest.close()

i = 1
data_map = {}
for msg in mailbox.mbox(mboxfile):
    print "processing message " + str(i)
    if not mail_utils.hasBody(msg):
        continue

    # YES or NO for having attachment
    has_attachment = False
    if mail_utils.hasAttachment(msg):
        has_attachment = True

    # write out the body of the email
    body = mail_utils.getPlainText(msg)
    data_map[i] = (body, has_attachment)

    i += 1

for key in data_map:
    print "key: " + str(key)
    print "val[0]: " + str(data_map[key][0])
    print "val[1]: " + str(data_map[key][1])

# dest.close()





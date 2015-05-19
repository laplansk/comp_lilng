import mailbox

def getcharsets(msg):
    charsets = set({})
    for c in msg.get_charsets():
        if c is not None:
            charsets.update([c])
    return charsets

def handleerror(errmsg, emailmsg, cs):
    print()
    print(errmsg)
    print("This error occurred while decoding with ",cs," charset.")
    print("These charsets were found in the one email.",getcharsets(emailmsg))
    print("This is the subject:",emailmsg['subject'])
    print("This is the sender:",emailmsg['From'])

def getbodyfromemail(msg):
    body = None
    #Only consider single part emails
    if not msg.is_multipart():
        body = msg.get_payload(decode=True)

   # No checking done to match the charset with the correct part.
    for charset in getcharsets(msg):
        try:
            body = body.decode(charset)
        except UnicodeDecodeError:
            continue
            # handleerror("UnicodeDecodeError: encountered.",msg,charset)
        except AttributeError:
            continue
            # handleerror("AttributeError: encountered" ,msg,charset)
    return body


mboxfile = '../mail_data/smallFile0.mbox'
print(mboxfile)
destFile = open('../mail_data/mailBodies0.txt', 'w')
mailNumber = 0
for thisemail in mailbox.mbox(mboxfile):

    body = getbodyfromemail(thisemail)
    if not body == None:

        try:
            destFile.write("\n//////////////  BEGIN_BODY" + str(mailNumber) + "/////////////\n")
            destFile.write(str(body))
            destFile.write("\n//////////////  END_BODY" + str(mailNumber) + "///////////////\n")
        except:
            continue
    mailNumber += 1

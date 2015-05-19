import sys
import mailbox

def gen_summary(filename):
    mbox = mailbox.mbox(filename)
    i = 1
    for message in mbox:

        subj = message['message']

        print("//////////BEGIN" + str(i) + "///////////////\n\n")
        print(message)
        print("///////////END" + str(i) + "////////////////\n\n")
        i = i + 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)

    gen_summary(sys.argv[1])
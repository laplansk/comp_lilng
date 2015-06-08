import re
import mailbox
import os
import io
import collections
import sys
import exceptions
import errno
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
    text_accum = ""
    payload = msg.get_payload()
    if msg.is_multipart():
        for subMsg in payload:
            if subMsg.get_content_type() == "text/plain":
                text_accum += subMsg.get_payload(decode=True)
        return text_accum
    else:
        if msg.get_content_type() == "text/plain":
            return msg.get_payload(decode=True)
        else:
            return ""

    # if msg.is_multipart():
    #     for part in msg.walk():
    #         if part.get_content_type() == "text/plain":
    #             return part.get_payload()
    # else:
    #     if msg.get_content_type() == "text/plain":
    #         return msg.get_payload()

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
        print("\n//////////////////////////" + str(item) + "//////////////////////////\n" +
              map[item][0] + "\n////////////////////////////////////////////////////\n" +
              str(map[item][1]))




def string_to_feature_vector(unigram_list, my_string):
    ret_list = [0] * len(unigram_list)
    for word in my_string.split():
        if word in unigram_list:
            # get the index
            ret_list[unigram_list.index(word)] += 1
        else:
            # TODO: throw away unknown words???
            continue
    return ret_list
# def get_bigram_vocab(print_output):


def get_unigram_counts(print_output):
    rootdir = "./mail_data/labeled_messages"
    cnt = collections.Counter()
    for subdir, dirs, files in os.walk(rootdir):
        numFilesToProcess = 500
        numFilesProcessed = 0
        for my_file in files:
            if numFilesProcessed >= numFilesToProcess:
                break
            try:
                with io.open(os.path.join(subdir, my_file), 'r', encoding='utf-8') as f:
                    try:
                        first_line = True
                        for line in f:
                            if first_line:
                                first_line = False
                                continue
                            else:
                                for word in line.split():
                                    cnt[word] += 1
                    except UnicodeDecodeError:
                        continue;
            except OSError:
                print("File not found")
            numFilesProcessed += 1

    if print_output:
        total_word_count = sum(cnt.values())
        print "total word count" + str(total_word_count)
        # for word, count in cnt.most_common(30):
        #     sys.stdout.write('{: < 6} {:<7.2%} {}\n'.format(count, float(count) / total_word_count, word.encode('utf8')))
    return cnt

def clean_unigrams(counter):
        # remove anything with count as low as 1
    for word, count in counter.items():
        if count <= 1 or "http" in word or "HTTP" in word:
            del counter[word]
    return counter
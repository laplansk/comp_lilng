import sys
import mailbox
import mail_utils
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)

# df_name = "mail_data/training_data.mail"
# unlikely_string = "#!#!#!#!\n"

# check that command line arg is valid filepath
mboxfile = sys.argv[1]
if not os.path.isfile(mboxfile):
    print('Invalid filepath - exiting')
    sys.exit(1)

print(mboxfile)

# analyze data in memory
num_messages = 0
num_yes = 0
num_no = 0
recall_yes_numerator = 0
precision_yes_numerator = 0

search_words1 = ["attachment", "attach", "attached", "attaching"]
search_words2 = ["include", "including", "included"]
search_words3 = ["add", "added", "adding"]
search_words4 = ["attachment", "attach", "attached", "attaching", "include", "including", "included", "add", "added", "adding"]
search_sets = (search_words1, search_words2, search_words3, search_words4)

for set in search_sets:
    search_words = set;
    for key in data_map:
        num_messages += 1
        if data_map[key][1] == True:
            num_yes += 1
        else:
            num_no += 1
        word_found = False
        for keyword in search_words:
            if keyword in data_map[key][0]:
                word_found = True
                break
        if word_found:
            recall_yes_numerator += 1
            if data_map[key][1] == True:
                precision_yes_numerator += 1

        word_found = False
    print "Testing the following keywords: "
    for word in search_words:
        print "\t" + word
    precision = float(precision_yes_numerator)/float(num_yes)
    recall = float(recall_yes_numerator)/float(num_yes)
    print "Precision: " + str(precision)
    print "Recall: " + str(recall)
    print "F-measure: " + str((2 * precision * recall)/(precision + recall))
    recall_yes_numerator = 0
    num_yes = 0







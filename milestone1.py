import sys
import mailbox
import mail_utils
import os.path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python parser.py [mbox file]')
        sys.exit(1)

# program vars
data_map = {}

mboxfile = sys.argv[1]
if not os.path.isfile(mboxfile):
    print('Invalid filepath - exiting')
    sys.exit(1)
else:
    data_map = mail_utils.loadFile(mboxfile)
    mail_utils.printMap(data_map)
    # print "size of map after function: " + str(len(data_map))

# Loop to allow for getting metrics over multiple gram sets
while True:
    gram_file = raw_input("Enter gram file: ")
    if not os.path.isfile(gram_file):
        print('Invalid filepath - try again')
        continue;
    else:
        gram_list = mail_utils.loadGrams(gram_file)
        gold_yes = 0
        gold_no = 0
        system_flagged_yes = 0          # anything our model flags as yes
        true_positives = 0      # anything the model and gold standard flag as yes

        # count emails with and without attachments
        for key in data_map:
            if data_map[key][1]:
                gold_yes += 1
            else:
                gold_no += 1

            # check whether or not this email contains one of the grams
            gram_found = False

            for gram in gram_list:
                if gram in data_map[key][0]:
                    gram_found = True
                    break
            if gram_found: # flagged by our system
                system_flagged_yes += 1
                if data_map[key][1]: # flagged by our system AND actually did have attachment
                    true_positives += 1
            gram_found = False
            # print results
        print "Testing the following grams: "
        for gram in gram_list:
            print "\t" + gram

        # check for divide-by-zeros
        precision = -1
        # How many selected items are relevant
        if not system_flagged_yes == 0:
            precision = float(true_positives)/float(system_flagged_yes)
        print "Precision: " + str(precision)

        # How many relevant items are selected
        recall = -1
        if not gold_yes == 0:
            recall = float(true_positives)/float(gold_yes)
        print "Recall: " + str(recall)

        # F_Measure with recall and precision equally weighted
        fMeasure = -1
        if not (precision + recall) == 0:
            fMeasure = (2 * precision * recall)/(precision + recall)
        print "F-measure: " + str(fMeasure)
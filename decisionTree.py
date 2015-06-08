import sys
import mail_utils
import os
import io

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('Usage: python parser.py')
        sys.exit(1)

# get unigram and bigram counts, store keys as a list and use those
# list indices as indices for the feature vectors later
unigram_counts = mail_utils.get_unigram_counts(True)
mail_utils.clean_unigrams(unigram_counts)
unigram_list = list(unigram_counts)

# get a list of feature vectors and class
rootdir = "./mail_data/labeled_messages"
i = 0
j = 0
features = []
outputs = []
for subdir, dirs, files in os.walk(rootdir):
    fileNo = 0
    numFilesToProcess = 500
    numFilesProcessed = 0
    for my_file in files:
        print str(j)
        j += 1
        first_line = True
        if numFilesProcessed >= numFilesToProcess:
            break
        plain_text = ""
        try:
            with io.open(os.path.join(subdir, my_file), 'r', encoding='utf-8') as f:
                try:
                    for line in f:
                        # get class value (always first line of file)
                        if first_line:
                            print str(i)
                            i += 1
                            if "True" in line:
                                outputs.append(True)
                            else:
                                outputs.append(False)

                            first_line = False
                        else:
                            # accumulate the rest of the message as a string
                            plain_text += line
                except UnicodeDecodeError as e:
                    print e
                    continue;

                # make a feature vector out of the string
                features.append(mail_utils.string_to_feature_vector(unigram_list, plain_text))
        except OSError:
            print("File not found")

        # print "processed fileNo: " + str(fileNo)
        fileNo += 1
        numFilesProcessed += 1

print "features size: " + str(len(features))
print "outputs size: " + str(len(outputs))


# mail_utils.string_to_feature_vector(unigram_list, "a craaaaaaaazy wooooooooords thaaaaaaaat aaaaaaren't reaaaaaaaal")


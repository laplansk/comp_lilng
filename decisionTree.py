import sys
import mail_utils
import os
import io
from sklearn import tree

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print('Usage: python parser.py')
        sys.exit(1)

# get unigram and bigram counts, store keys as a list and use those
# list indices as indices for the feature vectors later
unigram_counts = mail_utils.get_gram_counts(True)
mail_utils.clean_unigrams(unigram_counts)
unigram_list = list(unigram_counts)

# get a list of feature vectors and class
rootdir = "./mail_data/clean_labeled_messages_training"
training_features = []
training_outputs = []
outputNum = 0
featureNum = 0

###############################################
for subdir, dirs, files in os.walk(rootdir):
    for my_file in files:
        first_line = True
        plain_text = ""
        try:
            with io.open(os.path.join(subdir, my_file), 'r', encoding='utf-8') as f:
                try:
                    file_class = mail_utils.getClass(f)
                    training_outputs.append(file_class)
                    # print(str(file_class))
                    plain_text = mail_utils.getText(f)
                    # print(plain_text)
                    # outputNum += 1
                except UnicodeDecodeError as e:
                    print e
                    continue;
                # make a feature vector out of the string
                new_vec = mail_utils.string_to_feature_vector(unigram_list, plain_text)
                if new_vec is None:
                    print("None feature vector")

                training_features.append(new_vec)
                # print(str(featureNum))
                # featureNum += 1
        except OSError:
            print("File not found")

###############################################
# for subdir, dirs, files in os.walk(rootdir):
#     for my_file in files:
#         first_line = True
#         plain_text = ""
#         try:
#             with io.open(os.path.join(subdir, my_file), 'r', encoding='utf-8') as f:
#                 try:
#                     for line in f:
#                         # get class value (always first line of file)
#                         if first_line:
#                             print(str(outputNum))
#                             if "True" in line:
#                                 outputs.append(0)
#                             else:
#                                 outputs.append(1)
#                             first_line = False
#                             outputNum += 1
#                         else:
#                             # accumulate the rest of the message as a string
#                             plain_text += line
#                 except UnicodeDecodeError as e:
#                     print e
#                     continue;
#
#                 # make a feature vector out of the string
#                 new_vec = mail_utils.string_to_feature_vector(unigram_list, plain_text)
#                 if new_vec is None:
#                     print("None feature vector")
#
#                 features.append(new_vec)
#                 print(str(featureNum))
#                 featureNum += 1
#         except OSError:
#             print("File not found")

print "features size: " + str(len(training_features))
print "outputs size: " + str(len(training_outputs))

decisionTree = tree.DecisionTreeClassifier()
decisionTree = decisionTree.fit(training_features, training_outputs)




i = 0
for elem in training_features:
    if decisionTree.predict([elem]) == [0]:
        print("Attachment prediction")
        i += 1

print(str(i))

# now that tree is built, make predictions over test data and calculate precision and recall

true_positives = 0
gold_positives = 0
sys_positive = 0

for subdir, dirs, files in os.walk(rootdir):
    for my_file in files:
        first_line = True
        plain_text = ""
        try:
            with io.open(os.path.join(subdir, my_file), 'r', encoding='utf-8') as f:
                try:
                    file_class = mail_utils.getClass(f)
                    plain_text = mail_utils.getText(f)
                except UnicodeDecodeError as e:
                    print e
                    continue;
                if file_class == 0:
                    gold_positives += 1
                # make a feature vector out of the string
                new_vec = mail_utils.string_to_feature_vector(unigram_list, plain_text)
                if decisionTree.predict([elem]) == [0]: # True
                    sys_positive += 1
                    if file_class == 0:
                        true_positives += 1


        except OSError:
            print("File not found")

# check for divide-by-zeros
precision = -1
# How many selected items are relevant
if not sys_positive == 0:
    precision = float(true_positives)/float(sys_positive)
print "Precision: " + str(precision)

# How many relevant items are selected
recall = -1
if not gold_positives == 0:
    recall = float(true_positives)/float(gold_positives)
print "Recall: " + str(recall)

# F_Measure with recall and precision equally weighted
fMeasure = -1
if not (precision + recall) == 0:
    fMeasure = (2 * precision * recall)/(precision + recall)
print "F-measure: " + str(fMeasure)
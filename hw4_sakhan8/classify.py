## Sofia Khan CS 540
import math
from copy import deepcopy
from os import listdir
import glob, os
from os.path import basename
import numpy as np


###############################################Helper Methods###########################################################


def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    dicto = dict(list(zip(wordlist,wordfreq)))
    return dicto ## returns a dictionary!!

def sortFreqDict(freqdicto):
    aux = [key for key in freqdicto]
    aux.sort() ## sort this into given order
    return aux

###############################################Main Methods###########################################################

def create_vocabulary_attempt(training_directory, cutoff):
    # this was a failed attempt to create vocab.
    vocab = []
    for root, dirs, files in os.walk(training_directory):
            for file in files:
                if file.endswith(".txt"):
                    with open(os.path.join(root, file), "r") as f: # open each file up and traverse lines
                        for line in f:
                            line = line.rstrip()
                            vocab.append(line)
    vocab = wordListToFreqDict(vocab, cutoff)
    vocab = sortFreqDict(vocab)
    return vocab

def create_vocabulary(directory, cutoff):
    vocab = []
    for dirpath, dirnames, filename in os.walk(directory, topdown=True):
        for filename in filename:
            # create full path
            txtfile_full_path = os.path.join(dirpath, filename)
            with open(txtfile_full_path, encoding="utf8") as f:
                # print(txtfile_full_path)
                line = f.read().splitlines()
                vocab.append(line)
                # print(vocab)
    flat_list = []
    for sublist in vocab:
        for item in sublist:
            flat_list.append(item)
    # flat_list.sort()
    dupes = []
    unique = set(flat_list)
    for i in unique:
        if (flat_list.count(i) >= cutoff):
            dupes.append(i)
    vocab = dupes
    vocab.sort()

    return vocab

def create_bow(vocabulary, filePath):
    oov_count = 0
    dictwordsinfile = []

    with open(filePath, "r") as f:
        for line in f:
            stripped = line.rstrip()
            if stripped in vocabulary:
                dictwordsinfile.append(stripped)
            else:
                dictwordsinfile.append(None)

    bow = wordListToFreqDict(dictwordsinfile)
    return bow


#create and return training set (bag of words Python dictionary + label) from the files in a training directory
def load_training_data(vocab, directory):
    returnList = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            # print basename(root) this is the label
            filepath = root +'/'+ file
            dictionary = {}
            dictionary['label'] = basename(root)
            dictionary['bow'] = create_bow(vocab, filepath)
            returnList.append(dictionary)

    return returnList


def prior(training_data, label_list):
    prior = {}
    # print("Total number of training files: ", len(training_data))
    total_num_of_files = len(training_data);

    all_occurrences = []

    for item in training_data:
        if label_list.__contains__(item['label']):
            all_occurrences.append(item['label'])

    for label in label_list:
        n_files_with_label = all_occurrences.count(label) ## count how many times this label appeared
        n = n_files_with_label
        p_label = (n+1)/(total_num_of_files+2)
        # print("P label of ", label, "=", p_label)
        p_label = math.log(p_label)
        prior[label] = p_label

    return prior

# Training data looks like this:
# [{'label': '2020', 'bow': {'it': 1, 'is': 1, 'february': 1, '19': 1, ',': 1, '2020': 1, '.': 1}},
#     {'label': '2016', 'bow': {'hello': 1, 'world': 1}},
#     {'label': '2016', 'bow': {'a': 2, 'dog': 1, 'chases': 1, 'cat': 1, '.': 1}}]
def p_word_given_label_attempt(vocab, training_data, label):
    size_vocab = len(vocab)
    ## only use data w the good label
    good_data =[]
    the_vocabulary = vocab
    if (size_vocab >= 1 and vocab[size_vocab - 1] != None):
        vocab.append(None)

    for data in training_data:
        if(data['label'] == label):
            good_data.append(data)

    return_probs = {}
    for word in the_vocabulary:
        total_words_sum = 0
        word_appears_sum = 0
        for data in good_data:
            bow = data['bow']
            total_words_sum += sum(bow.values())
            if(bow.__contains__(word)):
                appears= bow[word]
                word_appears_sum += appears

        prob = (word_appears_sum+1)/(total_words_sum + size_vocab + 1)
        prob = math.log(prob)
        return_probs[word] = prob
    return return_probs


def p_word_given_label(vocab, training_data, label):
    word_prob = {}
    size_vocab = len(vocab)
    ## only use data w the good label
    match = []
    vocab = deepcopy(vocab)
    if (size_vocab >= 1 and vocab[size_vocab - 1] != None):
        vocab.append(None)
    # print(vocab)
    for i in training_data:
        if (i['label'] == label):
            match.append(i)
    # total = 0
    # count = 0
    for i in vocab:
        total = 0
        count = 0
        for j in match:
            bow = j['bow']
            # print(bow)
            total += sum(bow.values())
            if (bow.__contains__(i)):
                appears = bow[i]
                # print(bow)
                count += appears

        # prob = (count+1)/(total + size_vocab + 1)
        # prob = np.log(prob)
        a = count + 1
        b = total + size_vocab + 1
        loga = np.log(a)
        logb = np.log(b)
        prob = loga - logb
        word_prob[i] = prob
    # print(count)
    return word_prob

def train_1_fail(directory, cutoff):
    train = {}

    myvocabulary = create_vocabulary(directory, cutoff )
    # print('Vocabulary:' ,myvocabulary)

    training_data = load_training_data(myvocabulary, directory)
    # print("Training data:" , training_data)

    prior_output = prior(training_data, [2016, 2020])
    print('Prior output:' ,prior_output)

    p_2016 = p_word_given_label(myvocabulary, training_data, 2016)
    print('p_2016 = :' ,p_2016)

    p_2020 = p_word_given_label(myvocabulary, training_data, 2020)
    print('p_2020 = :' ,p_2020)

    return train


def train(training_directory, cutoff):
    training_return = {}

    vocabbb = create_vocabulary(training_directory, cutoff)
    # print("vocab is:" , vocab)
    training_return['vocabulary'] = create_vocabulary(training_directory, cutoff)

    training_data = load_training_data(vocabbb, training_directory)
    label_list = []
    for root, dirs, files in os.walk(training_directory):
        for file in files:
            filepath = root + '/' + file
            label_list.append(os.path.basename(root))
    label_list = list(dict.fromkeys(label_list))
    prior_return = prior(training_data, label_list)

    training_return['log prior'] = prior_return

    for i in label_list:
        training_return['log p(w|y=' + i + ')'] = p_word_given_label(vocabbb, training_data, i)

    return training_return

def classify(model, file):
    sum_2016 = 0
    sum_2020 = 0
    cond_probabilities_2016 = model['log p(w|y=2016)']
    cond_probabilities_2020 = model['log p(w|y=2020)']
    prior_probabilities = model['log prior']

    with open(file, "r") as f:  # open each file up and traverse lines
        for word in f:
            word = word.rstrip()
            #see if its in 2016:
            if word in cond_probabilities_2016:
                sum_2016 += cond_probabilities_2016[word]
            #see if its in 2020:
            if word in cond_probabilities_2020:
                sum_2020 += cond_probabilities_2020[word]
            #if its in neither
            else:
                sum_2016 += cond_probabilities_2016[None]
                sum_2020 += cond_probabilities_2020[None]

    sum_2016 += prior_probabilities['2016']
    sum_2020 += prior_probabilities['2020']

    results = {}
    results['log p(y=2016|x)'] = sum_2016
    results['log p(y=2020|x)'] = sum_2020

    if sum_2020 > sum_2016: ## 2020 had better results
        results['predicted y'] = '2020'
    else: ## 2016 had better results
        results['predicted y'] = '2016'

    return results

########################################################################################################################
#
# vocab= create_vocabulary('./EasyFiles/', 2)
# print (vocab)
# print (create_bow(vocab, './EasyFiles/2016/1.txt'))
# #
# print()
# vocab = create_vocabulary('./EasyFiles/', 1)
# x = load_training_data(vocab,'./EasyFiles/')
# print(x)
#

# print("Creating vocabulary...")
# #
# vocab = create_vocabulary('./corpus/training/', 2)
# # print ("Vocab: ", vocab )
# #
# training_data = load_training_data(vocab,'./corpus/training/')
# # print(training_data)
# #
# p = prior(training_data, ['2020', '2016'])
# print (p)

## log prior of word p

# vocab = create_vocabulary('./EasyFiles/', 2)
# # training_data = load_training_data(vocab, './EasyFiles/')
# # p = p_word_given_label(vocab, training_data, '2020')
# # print(p)
# #
# t = train('./EasyFiles/', 2)
# classified = classify(model, './corpus/test/2016/0.txt')
# print(classified)
#
# model = train('./corpus/training/', 2)
# classified = classify(model, './corpus/test/2016/0.txt')
# print(classified)


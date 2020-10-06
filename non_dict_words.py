import regex as re
from nltk.tokenize import WordPunctTokenizer
import string
from collections import Counter
import json
import os.path as osp

def non_dict_words(df):

    nonword = re.compile(r'^[\'.?!]|^U|\d\d\d\d')
    tokenizer = WordPunctTokenizer()
    non_dict_words = [[],[],[],[],[],[]]
    pony_words = [[],[],[],[],[],[]]
    dfs = df[df['pony_num'] != -1]
    for i, x in dfs.iterrows():
        words = tokenizer.tokenize(x[3])
        for word in words:
            if word not in string.punctuation and re.search(nonword, word) is None:
                pony_words[x[4]].append(word.strip().lower())  # adding the words to the corresponding pony's list

    dict_words = []
    script_dir = osp.dirname(__file__)
    d = osp.join(script_dir, '..', '..', 'data', 'words_alpha.txt')
    with open(d, 'r') as dictionary:
        for line in dictionary:
            dict_words.append(line.strip().lower())
        dict_set = set(dict_words)
        for i in range(6):
            for word in pony_words[i]:
                if word not in dict_set:
                    non_dict_words[i].append(word)

    finalvals = [[],[],[],[],[],[]]
    for i in range(6):
        non_dict_words[i] = Counter(non_dict_words[i]).most_common(5)
        for word in non_dict_words[i]:
            finalvals[i].append(word[0])

    ndw = {
        'twilight': finalvals[0],
        'applejack': finalvals[1],
        'rarity': finalvals[2],
        'pinkie': finalvals[3],
        'rainbow': finalvals[4],
        'fluttershy': finalvals[5],
    }

    # print(ndw)
    return ndw

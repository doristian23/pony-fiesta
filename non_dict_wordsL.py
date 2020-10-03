import regex as re
from nltk.tokenize import WordPunctTokenizer
import string
from collections import Counter

def main(df):

    nonword = re.compile(r'^[\'.?!]|U|\d\d\d\d')
    tokenizer = WordPunctTokenizer()
    non_dict_words = [[],[],[],[],[],[]]
    pony_words = [[],[],[],[],[],[]]
    dfs = df[df['pony_num'] != -1]
    for i, x in dfs.iterrows():
        words = tokenizer.tokenize(x[3])
        for word in words:
            if word not in string.punctuation and re.search(nonword, word) is None:
                pony_words[x[4]].append(word.strip().lower())

    dict_words = []
    with open(r'C:\Users\Admin\OneDrive\Documents\School\COMP 598\words_alpha.txt', 'r') as dictionary:
        for line in dictionary:
            dict_words.append(line.strip().lower())
            # print(line.strip())
        dict_set = set(dict_words)
        for i in range(6):
            for word in pony_words[i]:
                if word not in dict_set:
                    # print(word)
                    # return
                    non_dict_words[i].append(word)

    for i in range(6):
        non_dict_words[i] = Counter(non_dict_words[i])
        print(non_dict_words[i].most_common(5))



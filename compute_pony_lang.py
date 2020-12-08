import math
import json
import argparse
from itertools import islice


def get_tfidf(pony_dicts_gt5, num):
    num_of_words = 0
    pony_names = ['twilight', 'applejack', 'rarity', 'pinkie', 'rainbow', 'fluttershy']
    freq_w = {}
    freq_w_p = {}

    for i in range(6):
        p = pony_names[i]
        freq_w_p[p] = {}
        for word, count in pony_dicts_gt5[p].items():
            num_of_words += count
            if word in freq_w:
                freq_w[word] += count
            else:
                freq_w[word] = count
            if word in freq_w_p[p]:
                freq_w_p[p][word] += count
            else:
                freq_w_p[p][word] = count

    tfidf = {}
    tfidf_words = {}

    for i in range(6):
        p = pony_names[i]
        tfidf[p] = {}
        for word, count in pony_dicts_gt5[p].items():
            tfidf[p][word] = freq_w_p[p][word] * (math.log(num_of_words / freq_w[word]))
        # sorting[0:num+1]
        tfidf[p] = {k: v for k, v in sorted(tfidf[p].items(), key=lambda i: i[1], reverse=True)}
        tfidf_words[p] = list(tfidf[p].keys())[0:num]

    return tfidf_words


def get_tfidf_new(pony_dicts_gt5, num):
    num_of_words = 0
    pony_names = ['twilight', 'applejack', 'rarity', 'pinkie', 'rainbow', 'fluttershy']
    freq_w = {} # freq of each word in the entire corpus
    freq_w_p = {} # freq of each word for each pony
    freq_p_w = {} # number of ponies that say each word

    for i in range(6):
        p = pony_names[i]
        freq_w_p[p] = {}
        for word, count in pony_dicts_gt5[p].items():
            num_of_words += count
            if word in freq_w:
                freq_w[word] += count
            else:
                freq_w[word] = count
            if word in freq_w_p[p]:
                freq_w_p[p][word] += count
            else:
                freq_w_p[p][word] = count

    for word in freq_w.keys():
         for i in range(6):
             p = pony_names[i]
             if word in freq_w_p[p]:
                if word in freq_p_w:
                    freq_p_w[word] += 1
                else:
                    freq_p_w[word] = 1

    tfidf = {}
    tfidf_words = {}

    for i in range(6):
        p = pony_names[i]
        tfidf[p] = {}
        for word, count in pony_dicts_gt5[p].items():
            tfidf[p][word] = freq_w_p[p][word] * (math.log(6/ freq_p_w[word]))
        tfidf[p] = {k: v for k, v in sorted(tfidf[p].items(), key=lambda i: i[1], reverse=True)}
        tfidf_words[p] = list(tfidf[p].keys())[0:num]

    return tfidf_words


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store_true', help="alternate tfidf computation")
    parser.add_argument('word_counts', help="pony word counts")
    parser.add_argument('num_words', help="number of words to output per pony")

    args = parser.parse_args()
    with open(args.word_counts, 'r') as infile:
        pony_dicts = json.load(infile)
        if args.p is False:
            words = get_tfidf(pony_dicts, int(args.num_words))
            print(json.dumps(words, indent=4))
        else:
            words = get_tfidf_new(pony_dicts, int(args.num_words))
            print(json.dumps(words, indent=4))



if __name__ == "__main__":
    main()
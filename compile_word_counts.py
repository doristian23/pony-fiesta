import argparse
import pandas as pd
import json
import regex as re
from collections import Counter


def get_words(dialog_file):
    with open(dialog_file, 'r') as infile:
        df = pd.read_csv(infile)
        names = ['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Rainbow Dash', 'Fluttershy']

        pony_dicts = []
        for i in range(6):
            pony_dicts.append(Counter())

        for i, x in df.iterrows():
            for n, e in enumerate(names):
                if x[2] == names[n]:
                    punct = r'[^\w\s\']'
                    text = x[3]
                    new_text = re.sub(punct, ' ', text)
                    new_text = new_text.lower()
                    words = new_text.split()
                    words = [word for word in words if word.isalpha()]
                    pony_dicts[n].update(words)

        pony_dicts_gt5 = {}
        pony_names = ['twilight', 'applejack', 'rarity', 'pinkie', 'rainbow', 'fluttershy']
        for i in range(6):
            new_dict = {key: val for key, val in pony_dicts[i].items() if val >= 5}
            pony_dicts_gt5[pony_names[i]] = new_dict

        return pony_dicts_gt5


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help="output file", required=True)
    parser.add_argument('dialog', help="clean_dialog.csv file")

    args = parser.parse_args()

    pony_word_dicts = get_words(args.dialog)

    with open(args.o, 'w') as outfile:
        json.dump(pony_word_dicts, outfile, indent=4)


if __name__ == "__main__":
    main()


import argparse
import pandas as pd
from hw3.mentions import mentions
from hw3.verbosity import verbosity
from hw3.follow_on import follow_on
from hw3.non_dict_words import non_dict_words
import json
import sys
import os.path as osp

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', help="optional name of json output file; will output to stdout if left blank")

    args = parser.parse_args()

    # dataframe = pd.read_csv(r"C:\Users\Admin\OneDrive\Documents\School\COMP 598\HW3\clean_dialog.csv")
    
    script_dir = osp.dirname(__file__)

    src_file = osp.join(script_dir, '..', 'data', 'clean_dialog.csv')
 
    dataframe = pd.read_csv(src_file)
    ndf, ver = verbosity(dataframe)
    men = mentions(ndf)
    fol = follow_on(ndf)
    non = non_dict_words(ndf)

    vals = {
        'verbosity': ver,
        'mentions': men,
        'follow_on_comments': fol,
        'non_dictionary_words': non,
    }

    if args.o is not None:
        filename = args.o
        with open(filename, 'w') as outfile:  # datafile is given as optional arg in command line
            json.dump(vals, outfile, indent=4)
    else:
        out_vals = json.dumps(vals, indent=4)
        print(out_vals)


if __name__ == "__main__":
    main()



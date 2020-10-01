import regex as re
import json

def main(df):

    total_lines = float(len(df.index))  # index does not count header!

    neg = re.compile("except|but|sans")
    more = re.compile("and")
    tw = re.compile(r'Twilight Sparkle')
    aj = re.compile(r'Applejack')
    ra = re.compile(r'Rarity')
    pp = re.compile(r'Pinkie Pie')
    rd = re.compile(r'Rainbow Dash')
    fs = re.compile(r'Fluttershy')
    exps = [tw, aj, ra, pp, rd, fs]

    verbo_vals = [0, 0, 0, 0, 0, 0]
    speaker = []
    spoke_last = None

    for i, x in df.iterrows():
        speaker.append([])
        if re.search(more, x[2]) is not None:
            for n, e in enumerate(exps):
                if re.search(e, x[2]) is not None:
                    verbo_vals[n] += 1
                    speaker[i].append(n)
                    spoke_last = None
        elif re.search(neg, x[2]) is None:  # if no except/but/sans
            if re.search("All", x[2]) is not None:
                for a in range(6): verbo_vals[a] +=1
                speaker[i].extend([0, 1, 2, 3, 4, 5])
                spoke_last = None
            else:
                for n, e in enumerate(exps):
                    s = re.search(e, x[2])
                    if (s is not None) and (s != spoke_last):
                        verbo_vals[n] += 1
                        speaker[i].append(n)
                        spoke_last = s
                        break
        else:  # if yes except/but/sas
            for n, e in enumerate(exps):
                if re.search(e, x[2]) is None:  # ponies that aren't mentioned are the speakers
                    verbo_vals[n] += 1
                    speaker[i].append(n)  
                    spoke_last = None

    verbosity_vals = {
        'twilight': verbo_vals[0]/total_lines,
        'applejack': verbo_vals[1]/total_lines,
        'rarity': verbo_vals[2]/total_lines,
        'pinkie': verbo_vals[3]/total_lines,
        'rainbow': verbo_vals[4]/total_lines,
        'fluttershy': verbo_vals[5]/total_lines}

    # verbosity: json + print
    with open('datafile.json', 'w') as outfile:  # datafile is given as optional arg in command line
        json.dump(verbosity_vals, outfile)

    verbosity = json.dumps(verbosity_vals, indent=4)
    print(verbosity)

    print(len(speaker))
    for i in range(6):
        print(verbo_vals[i] / total_lines)

    df.insert(4, 'pony_num', speaker)
    df.to_csv("new_dialogue.csv", index=False)

    # return df




"""
    
    
    
     # non_dictionary_words
    all_w = [[], [], [], [], [], []]
    non_d_w = [[], [], [], [], [], []]

    for i, x in df.iterrows():
        words = re.findall(r'\w+', x[3])
        for j in range(6):
            if i in x[4]:
                all_w[j].append(words)

     #  go thru each pony's list, remove dict words
"""




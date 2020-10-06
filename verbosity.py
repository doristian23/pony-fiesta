import regex as re
import json

def verbosity(df):

    total_lines = 0.0  # index does not count header!

    # neg = re.compile("except|but|sans")
    more = re.compile("and")
    tw = re.compile(r'^Twilight Sparkle', re.IGNORECASE)
    aj = re.compile(r'^Applejack', re.IGNORECASE)
    ra = re.compile(r'^Rarity', re.IGNORECASE)
    pp = re.compile(r'^Pinkie Pie', re.IGNORECASE)
    rd = re.compile(r'^Rainbow Dash', re.IGNORECASE)
    fs = re.compile(r'^Fluttershy', re.IGNORECASE)
    exps = [tw, aj, ra, pp, rd, fs]

    verbo_vals = [0, 0, 0, 0, 0, 0]
    speaker = []
    spoke_last = -1

    for i, x in df.iterrows():
        speaker.append(-1)
        for n, e in enumerate(exps):
            if re.search(more, x[2]) is not None:
                break
            s = re.search(e, x[2])
            # 1) found a pony name and 2a) didn't speak last or 2b) the speech acts occurred over different episodes
            if s is not None: speaker[i] = n
            if (s is not None) and ((n != spoke_last) or (i == 0 or (df.iloc[i, 0] != df.iloc[i-1, 0]))):
                verbo_vals[n] += 1
                speaker[i] = n
                spoke_last = n
                total_lines += 1
                break

    verbosity_vals = {
        'twilight': round(verbo_vals[0]/total_lines, 2),
        'applejack': round(verbo_vals[1]/total_lines, 2),
        'rarity': round(verbo_vals[2]/total_lines, 2),
        'pinkie': round(verbo_vals[3]/total_lines, 2),
        'rainbow': round(verbo_vals[4]/total_lines, 2),
        'fluttershy': round(verbo_vals[5]/total_lines, 2)
    }

    # verbosity: json + print
    # with open('verbosity.json', 'w') as outfile:  # datafile is given as optional arg in command line
        # json.dump(verbosity_vals, outfile, indent=4)

    # verbosity = json.dumps(verbosity_vals, indent=4)
    # print(verbosity)

    # print(len(speaker))
    # for i in range(6):
        # print(verbo_vals[i] / total_lines)

    df.insert(4, 'pony_num', speaker)
    # df.to_csv("new_dialogue.csv", index=False)

    return df, verbosity_vals




"""
    
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




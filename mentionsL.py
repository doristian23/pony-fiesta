import regex as re

def main(df):
    tw_m = re.compile("Twilight|Sparkle")
    aj_m = re.compile("Applejack")
    ra_m = re.compile("Rarity")
    pp_m = re.compile("Pinkie|Pie")
    rd_m = re.compile("Rainbow|Dash")
    fs_m = re.compile("Fluttershy")
    exps_m = [tw_m, aj_m, ra_m, pp_m, rd_m, fs_m]

    mentions_vals = [[], [], [], [], [], []]
    total_mentions = [0, 0, 0, 0, 0, 0]

    pony_names = {
        0: 'twilight',
        1: 'applejack',
        2: 'rarity',
        3: 'pinkie',
        4: 'rainbow',
        5: 'fluttershy',
    }

    for n in range(6):
        # creating a temp df for every pony
        dfs = df[df['pony_num'] == n]

        # counting mentions of each pony, by current pony n
        mentions_vals[n].extend([0, 0, 0, 0, 0, 0])
        for i, x in dfs.iterrows():
            for m, e1 in enumerate(exps_m):  # looping through the mentions regex
                if n != m and re.search(e1, x[3]) is not None:
                    num = len(re.findall(e1, x[3]))
                    mentions_vals[n][m] += num  # tallying up the # of times pony n mentions pony m
                    total_mentions[n] += num  # total number of times pony n mentions any other pony

    for i in range(6):
        print(pony_names[i])
        if total_mentions[i] == 0:
            for j in range(6): print(0.0)
        else:
            for j in range(6):
                if i != j:
                    print(pony_names[j]+": ", end='')
                    print(mentions_vals[i][j] / float(total_mentions[i]))
        print()

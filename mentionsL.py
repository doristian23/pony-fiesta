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

    for n in range(6):
        # creating a temp df for every pony, where the 5th column holds a bool if that pony speaks in this dialog
        single_speaker = []
        for i, x in df.iterrows():
            if str(n) in x[4]:
                single_speaker.append(True)
            else:
                single_speaker.append(False)
        df.insert(5, 'single_pony', single_speaker)
        dfs = df[df['single_pony'] == True]

        # counting mentions of each pony, by current pony n
        mentions_vals[n].extend([0, 0, 0, 0, 0, 0])
        for i, x in dfs.iterrows():
            for m, e1 in enumerate(exps_m):  # looping through the mentions regex
                if n != m and re.search(e1, x[3]) is not None:
                    mentions_vals[n][m] += 1  # tallying up the # of times pony n mentions pony m
                    total_mentions[n] += 1  # total number of times pony n mentions any other pony

        df = df.drop(columns=['single_pony'])

    for i in range(6):
        print(i)
        if total_mentions[i] == 0:
            for j in range(6): print(0.0)
        else:
            for j in range(6):
                if i != j:
                    print(mentions_vals[i][j] / float(total_mentions[i]))


import regex as re
import json

def mentions(df):
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
    m_vals = {}
    if total_mentions[0] != 0.0:
        m_vals['twilight'] = {
            'applejack': round(mentions_vals[0][1] / float(total_mentions[0]), 2),
            'rarity': round(mentions_vals[0][2] / float(total_mentions[0]), 2),
            'pinkie': round(mentions_vals[0][3] / float(total_mentions[0]), 2),
            'rainbow': round(mentions_vals[0][4] / float(total_mentions[0]), 2),
            'fluttershy': round(mentions_vals[0][5] / float(total_mentions[0]), 2),
        }
    else:
        m_vals['twilight'] = {
            'applejack': 0.0,
            'rarity': 0.0,
            'pinkie': 0.0,
            'rainbow': 0.0,
            'fluttershy': 0.0,
        }
    if total_mentions[1] != 0.0:
        m_vals['applejack'] = {
            'twilight': round(mentions_vals[1][0] / float(total_mentions[1]), 2),
            'rarity': round(mentions_vals[1][2] / float(total_mentions[1]), 2),
            'pinkie': round(mentions_vals[1][3] / float(total_mentions[1]), 2),
            'rainbow': round(mentions_vals[1][4] / float(total_mentions[1]), 2),
            'fluttershy': round(mentions_vals[1][5] / float(total_mentions[1]), 2),
        }
    else:
        m_vals['applejack'] = {
            'twilight': 0.0,
            'rarity': 0.0,
            'pinkie': 0.0,
            'rainbow': 0.0,
            'fluttershy': 0.0,
        }
    if total_mentions[2] != 0.0:
        m_vals['rarity'] = {
            'twilight': round(mentions_vals[2][0] / float(total_mentions[2]), 2),
            'applejack': round(mentions_vals[2][1] / float(total_mentions[2]), 2),
            'pinkie': round(mentions_vals[2][3] / float(total_mentions[2]), 2),
            'rainbow': round(mentions_vals[2][4] / float(total_mentions[2]), 2),
            'fluttershy': round(mentions_vals[2][5] / float(total_mentions[2]), 2),
        }
    else:
        m_vals['rarity'] = {
            'twilight': 0.0,
            'applejack': 0.0,
            'pinkie': 0.0,
            'rainbow': 0.0,
            'fluttershy': 0.0,
        }
    if total_mentions[3] != 0.0:
        m_vals['pinkie'] = {
            'twilight': round(mentions_vals[3][0] / float(total_mentions[3]), 2),
            'applejack': round(mentions_vals[3][1] / float(total_mentions[3]), 2),
            'rarity': round(mentions_vals[3][2] / float(total_mentions[3]), 2),
            'rainbow': round(mentions_vals[3][4] / float(total_mentions[3]), 2),
            'fluttershy': round(mentions_vals[3][5] / float(total_mentions[3]), 2),
        }
    else: m_vals['pinkie'] = {
            'twilight': 0.0,
            'applejack': 0.0,
            'rarity': 0.0,
            'rainbow': 0.0,
            'fluttershy': 0.0,
        }
    if total_mentions[4] != 0.0:
        m_vals['rainbow'] = {
            'twilight': round(mentions_vals[4][0] / float(total_mentions[4]), 2),
            'applejack': round(mentions_vals[4][1] / float(total_mentions[4]), 2),
            'rarity': round(mentions_vals[4][2] / float(total_mentions[4]), 2),
            'pinkie': round(mentions_vals[4][3] / float(total_mentions[4]), 2),
            'fluttershy': round(mentions_vals[4][5] / float(total_mentions[4]), 2),
        }
    else: m_vals['rainbow'] = {
            'twilight': 0.0,
            'applejack': 0.0,
            'rarity': 0.0,
            'pinkie': 0.0,
            'fluttershy': 0.0,
        }
    if total_mentions[5] != 0.0:
        m_vals['fluttershy'] = {
            'twilight': round(mentions_vals[5][0] / float(total_mentions[5]), 2),
            'applejack': round(mentions_vals[5][1] / float(total_mentions[5]), 2),
            'rarity': round(mentions_vals[5][2] / float(total_mentions[5]), 2),
            'pinkie': round(mentions_vals[5][3] / float(total_mentions[5]), 2),
            'rainbow': round(mentions_vals[5][4] / float(total_mentions[5]), 2),
        }
    else: m_vals['fluttershy'] = {
            'twilight': 0.0,
            'applejack': 0.0,
            'rarity': 0.0,
            'pinkie': 0.0,
            'rainbow': 0.0,
        }

    # with open('mentions.json', 'w') as outfile:  # datafile is given as optional arg in command line
        # json.dump(m_vals, outfile, indent=4)

    # mentions = json.dumps(m_vals, indent=4)
    # print(mentions)

    return m_vals

"""
       pony_names = {
        0: 'twilight',
        1: 'applejack',
        2: 'rarity',
        3: 'pinkie',
        4: 'rainbow',
        5: 'fluttershy',
    }
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
"""

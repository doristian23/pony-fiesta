import json

def follow_on(df):
    # counts the # of times a single pony says a line following another single pony AND
    # the # of times a single pony says a line following any other character, including several ponies & narrator

    follow_vals = [[], [], [], [], [], []]
    total_lines_per_pony = [0, 0, 0, 0, 0, 0]
    for i in range(6): follow_vals[i].extend([0, 0, 0, 0, 0, 0, 0])

    for i, x in df.iterrows():
        ponynum = x[4]
        if ponynum >= 0 and (df.iloc[i, 4] != df.iloc[i-1, 4]) and (df.iloc[i, 0] == df.iloc[i-1, 0]):
            prevspeaker = df.iloc[i - 1, 4]
            if prevspeaker >= 0 and prevspeaker != ponynum:
                follow_vals[ponynum][prevspeaker] += 1
                total_lines_per_pony[ponynum] += 1
            elif prevspeaker == -1:
                follow_vals[ponynum][6] += 1
                total_lines_per_pony[ponynum] += 1

    # for i in range(6):
        # print(total_lines_per_pony[i])
        # print(follow_vals[i])


    follow_on_vals = {
        'twilight': {
            'applejack': round(follow_vals[0][1]/total_lines_per_pony[0], 2),
            'rarity': round(follow_vals[0][2] / total_lines_per_pony[0], 2),
            'pinkie': round(follow_vals[0][3] / total_lines_per_pony[0], 2),
            'rainbow': round(follow_vals[0][4] / total_lines_per_pony[0], 2),
            'fluttershy': round(follow_vals[0][5] / total_lines_per_pony[0], 2),
            'other': round(follow_vals[0][6] / total_lines_per_pony[0], 2),
        },
        'applejack': {
            'twilight': round(follow_vals[1][0] / total_lines_per_pony[1], 2),
            'rarity': round(follow_vals[1][2] / total_lines_per_pony[1], 2),
            'pinkie': round(follow_vals[1][3] / total_lines_per_pony[1], 2),
            'rainbow': round(follow_vals[1][4] / total_lines_per_pony[1], 2),
            'fluttershy': round(follow_vals[1][5] / total_lines_per_pony[1], 2),
            'other': round(follow_vals[1][6] / total_lines_per_pony[1], 2),
        },
        'rarity': {
            'twilight': round(follow_vals[2][0] / total_lines_per_pony[2], 2),
            'applejack': round(follow_vals[2][1] / total_lines_per_pony[2], 2),
            'pinkie': round(follow_vals[2][3] / total_lines_per_pony[2], 2),
            'rainbow': round(follow_vals[2][4] / total_lines_per_pony[2], 2),
            'fluttershy': round(follow_vals[2][5] / total_lines_per_pony[2], 2),
            'other': round(follow_vals[2][6] / total_lines_per_pony[2], 2),
        },
        'pinkie': {
            'twilight': round(follow_vals[3][0] / total_lines_per_pony[3], 2),
            'applejack': round(follow_vals[3][1] / total_lines_per_pony[3], 2),
            'rarity': round(follow_vals[3][2] / total_lines_per_pony[3], 2),
            'rainbow': round(follow_vals[3][4] / total_lines_per_pony[3], 2),
            'fluttershy': round(follow_vals[3][5] / total_lines_per_pony[3], 2),
            'other': round(follow_vals[3][6] / total_lines_per_pony[3], 2),
        },
        'rainbow': {
            'twilight': round(follow_vals[4][0] / total_lines_per_pony[4], 2),
            'applejack': round(follow_vals[4][1] / total_lines_per_pony[4], 2),
            'rarity': round(follow_vals[4][2] / total_lines_per_pony[4], 2),
            'pinkie': round(follow_vals[4][3] / total_lines_per_pony[4], 2),
            'fluttershy': round(follow_vals[4][5] / total_lines_per_pony[4], 2),
            'other': round(follow_vals[4][6] / total_lines_per_pony[4], 2),
        },
        'fluttershy': {
            'twilight': round(follow_vals[5][0] / total_lines_per_pony[5], 2),
            'applejack': round(follow_vals[5][1] / total_lines_per_pony[5], 2),
            'rarity': round(follow_vals[5][2] / total_lines_per_pony[5], 2),
            'pinkie': round(follow_vals[5][3] / total_lines_per_pony[5], 2),
            'rainbow': round(follow_vals[5][4] / total_lines_per_pony[5], 2),
            'other': round(follow_vals[5][6] / total_lines_per_pony[5], 2),
        },
    }

    # with open('follow_on_comments.json', 'w') as outfile:  # datafile is given as optional arg in command line
        # json.dump(follow_on_vals, outfile, indent=4)

    # follows = json.dumps(follow_on_vals, indent=4)
    # print(follows)

    return follow_on_vals

"""
        if len(ponynum) == 3:
            c = ponynum[1]
            total_lines_per_pony[int(c)] +=1
            prevspeaker = df.iloc[i-1, 4]
            if len(prevspeaker) == 3:
                p = prevspeaker[1]
                follow_vals[int(c)][int(p)] += 1
            else:
                follow_vals[int(c)][6] += 1
"""

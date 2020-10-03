def main(df):
    # counts the # of times a single pony says a line following another single pony AND
    # the # of times a single pony says a line following any other character, including several ponies & narrator

    follow_vals = [[], [], [], [], [], []]
    total_lines_per_pony = [0, 0, 0, 0, 0, 0]
    for i in range(6): follow_vals[i].extend([0, 0, 0, 0, 0, 0, 0])

    for i, x in df.iterrows():
        ponynum = x[4]
        if ponynum >= 0:
            total_lines_per_pony[ponynum] += 1
            prevspeaker = df.iloc[i - 1, 4]
            if prevspeaker >= 0:
                follow_vals[ponynum][prevspeaker] += 1
            else:
                follow_vals[ponynum][6] += 1

    for i in range(6):
        print(total_lines_per_pony[i])
        print(follow_vals[i])


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

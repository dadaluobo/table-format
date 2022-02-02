import pandas as pd


def print_table_pretty(dfOrig):
    # sample
    # +----+-----------+-------------+
    # |    |   col_two | column_3    |
    # |----+-----------+-------------|
    # |  0 |    0.0001 | ABCD        |
    # |  1 |    1e-05  | ABCD        |
    # |  2 |    1e-06  | long string |
    # |  3 |    1e-07  | ABCD        |
    # +----+-----------+-------------+

    df = dfOrig.astype(str)
    outStr = ""
    cols = list(df.columns)
    height, width = df.shape

    maxCharLen = [len(x) for x in cols]
    for index, row in df.iterrows():
        rowCharLen = [len(x) for x in row]
        for i in range(width):
            if rowCharLen[i] > maxCharLen[i]:
                maxCharLen[i] = rowCharLen[i]

    targetCharLen = [(x + 4) for x in maxCharLen]
    boundary = "+"
    for i in range(width):
        boundary += "-" * targetCharLen[i] + "+"

    outStr += boundary + "\n"
    head = "|"
    for i in range(width):
        head += cols[i].center(targetCharLen[i]) + "|"
    outStr += head + "\n" + boundary + "\n"
    body = ""
    for index, row in df.iterrows():
        body += "|"
        for i in range(width):
            body += row[i].center(targetCharLen[i]) + "|"
        body += "\n"
    outStr += body + boundary + "\n"

    return outStr


if __name__ == '__main__':
    df = pd.read_csv("letter_frequency.txt")
    print(print_table_pretty(df))

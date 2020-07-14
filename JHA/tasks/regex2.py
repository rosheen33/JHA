# -*- coding: utf-8 -*-
import csv
import re

# 'Bonus: Is there a single regex for all 5 examples ?'
# We can use the 1 regex for first 4 values which are in cm

# Answer regex
# 1: '(?P<h>[.,\d]+)[cm]*\s*[×|x]\s*(?P<w>[.,\d]+)\s*[cm]*[×|x]*\s*(?P<d>[.,\d]*)\s*[cm]'
# 2: '(?P<h>[.\d]+)\s*by\s*(?P<w>[.\d]+)\s*in'


def main():
    with open('Data_Engineer_test/candidateEvalData/dim_df_correct.csv') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)

        for row in spamreader:
            if 'cm' in row[0]:
                regex = '(?P<h>[.,\d]+)[cm]*\s*[×|x]\s*(?P<w>[.,\d]+)\s*[cm]*[×|x]*\s*(?P<d>[.,\d]*)\s*[cm]'
                print('RAW DIM')
                print(row[0])
                match = re.findall(regex, row[0])
                match = [float(m.replace(',', '.')) if m else 0 for m in match[-1]]
                print("HEIGHT, WIDTH, DEPTH")
                print(match)
            else:
                # value is in inch
                regex = '(?P<h>[.\d]+)\s*by\s*(?P<w>[.\d]+)\s*in'
                print('RAW DIM')
                print(row[0])
                match = re.search(regex, row[0])
                print("HEIGHT, WIDTH, DEPTH")
                print('[{}, {}]'.format(float(match.group('h')) * 2.54, float(match.group('w')) * 2.54))


if __name__ == "__main__":
    main()

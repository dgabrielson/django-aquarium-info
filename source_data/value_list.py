"""
Analyze key frequencies in all *.pickle files
"""

import cPickle as pickle
import sys


def main(keyname, filename):
    values = set()
    with open(filename) as f:
        data = pickle.load(f)
        for record in data:
            for key in record.keys():
                if key == keyname:
                    values.add(record[key])
    return values


if __name__ == '__main__':
    key, filename = sys.argv[1:]
    values = main(key, filename)
    print ', '.join(values)

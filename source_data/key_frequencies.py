"""
Analyze key frequencies in all *.pickle files
"""
import cPickle as pickle
import glob
import sys
from pprint import pprint


def main(filename):
    result = {}
    values = {}
    with open(filename) as f:
        data = pickle.load(f)
        for record in data:
            for key in record.keys():
                if key not in result:
                    result[key] = [0, 0]
                if key not in values:
                    values[key] = set()
                result[key][0] += 1
                values[key].add(record[key])
    for key in result:
        result[key][1] = len(values[key])
    return result


if __name__ == '__main__':
    filename_list = sys.argv[1:]
    if not filename_list:
        filename_list = glob.glob('*.pickle')
        
    for filename in filename_list:
        frequencies = main(filename)
        print filename
        pprint(frequencies)
        print

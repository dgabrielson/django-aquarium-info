"""
Requires model map file.
"""
import cPickle as pickle
import glob

from value_list import main as value_list


def get_all_values(key, pickle_files):
    values = []
    for pickle in pickle_files:
        values.extend( value_list(key, pickle) )
    values = list(set(values))
    values.sort()
    return values
    
    
def save(model, values):
    with open('{model}.values'.format(**locals()), 'w') as f:
        for v in values:
            f.write('{v}\n'.format(**locals()))


def main(modelmap_filename):
    pickle_files = glob.glob('*.pickle')
    with open(modelmap_filename) as f:
        for line in f:
            if not line.strip():
                continue
            key, model = [ e.strip() for e in line.split(':') ]
            values = get_all_values(key, pickle_files)
            print model, values
            save(model, values)

if __name__ == '__main__':
    main('fk_model_map.txt')

"""
Extract html files into a pythonic data structure.
"""

import cPickle as pickle
import glob
import os
import sys
from pprint import pprint

import get_page


def do_div(div_source):
    """
    div source is assumed to contain some pretext, followed by a ul
    of li key: items.
    """
    ul_pos = div_source.find('<ul>')
    assert ul_pos != -1, 'Unexpected div_source format: ' + repr(div_source)
    upto = get_page.strip_html(div_source[:ul_pos]).strip()
    ul_list = get_page.get_chunks(div_source, '<ul>', '</ul>')
    assert len(ul_list) == 1, 'Wrong number of ul fragments in div_source: ' + repr(div_source)
    ul = ul_list[0]
    li_list = [ e[4:-5] for e in get_page.get_chunks(ul, '<li>', '</li>') ]
    data = {}
    for li in li_list:
        pos = li.find(':')
        assert pos != -1, 'Unexpected li format: ' + repr(li)
        data[li[:pos].strip()] = li[pos+1:].strip()
    # the upto string is always the same: #NN. key: value
    # so fold that into the data dictionary:
    pos_p = upto.find('.')
    assert pos_p != -1, 'Unexpected upto format (1): ' + repr(upto)
    pos_c = upto.find(':')
    assert pos_c != -1, 'Unexpected upto format (2): ' + repr(upto)
    assert pos_p < pos_c, 'Unexpected upto format (3): ' + repr(upto)
    key = upto[pos_p+1:pos_c].strip()
    value = upto[pos_c+1:].strip()
    data[key] = value
    return data
    

def main(filename):
    """
    Filename is assumed to contain html fragment: a list of div tags.
    """
    results = []
    with open(filename) as f:
        source_text = f.read()
        div_list = get_page.get_chunks(source_text, '<div>', '</div>')
        for div in div_list:
            div_int = div[5:-6]
            results.append( do_div(div_int) )
    return results


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        args = glob.glob('*.html')
    for arg in args:
        data = main(arg)
        if sys.stdout.isatty():
            pprint(data)
        else:
            pickle.dump(data, sys.stdout)

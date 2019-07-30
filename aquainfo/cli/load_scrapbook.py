"""
CLI list for aquainfo
"""
#######################################################################

HELP_TEXT = __doc__.strip()
DJANGO_COMMAND = 'main'
OPTION_LIST = ()
ARGS_USAGE = 'ModelFile.pickle [...]'

#######################################################################

import cPickle as pickle
import os

from django.db import models
from django.template.defaultfilters import slugify

from scrapbook.models import Link, Picture

from .load_info_items import extract_name_href

#from aquainfo.models import FreshwaterFish, FreshwaterPlant


#######################################################################

def do_model_record(model_class, record):
    if model_class.__name__ == 'FreshwaterFish':
        key = 'Common name'
    elif model_class.__name__ == 'FreshwaterPlant':
        key = 'Plant name'
    else:
        assert False, 'cannot deal with this model'
    name, href = extract_name_href(record[key])
    photo_url = record['Photo URL']
    slug = slugify(name)
    try:
        fish = model_class.objects.get(slug=slug)
    except FreshwaterFish.DoesNotExist:
        pass
    else:
        label = 'aqua-fish.net'
        if href is not None:
            link, created = Link.objects.get_or_create_for_model(model=fish, title=label, target=href)
            print link
        picture = Picture.objects.create_from_url(model=fish, url=photo_url, caption=label)
        print picture
        picture.save()

#######################################################################

def do_modelfile(model_filename):

    app_label = os.path.split(os.path.dirname(
                            os.path.dirname(os.path.abspath(__file__))))[-1]

    basename = os.path.split(model_filename)[-1]
    modelname = os.path.splitext(basename)[0]

    model = models.get_model(app_label, modelname)
    if model is None:
        print '[!!!] Model "{modelname}" not found!'.format(**locals())
        return

    with open(model_filename) as f:
        records = pickle.load(f)
        for record in records:
            do_model_record(model, record)
                
    

#######################################################################

def main(options, args):
    for arg in args:
        do_modelfile(arg)    

    
#######################################################################

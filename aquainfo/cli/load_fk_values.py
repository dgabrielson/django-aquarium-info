"""
CLI list for aquainfo
"""
#######################################################################

HELP_TEXT = __doc__.strip()
DJANGO_COMMAND = 'main'
OPTION_LIST = ()
ARGS_USAGE = 'ModelFile.model [...]'


#######################################################################

import os

from django.db import models
from django.template.defaultfilters import slugify

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
        for line in f:
            name = line.strip()
            if not name:
                continue
            slug = slugify(name)
            obj, created = model.objects.get_or_create(name=name, slug=slug)
            if created:
                print 'Created {modelname}: {obj}'.format(**locals())
    

#######################################################################

def main(options, args):
    for arg in args:
        do_modelfile(arg)    

    
#######################################################################

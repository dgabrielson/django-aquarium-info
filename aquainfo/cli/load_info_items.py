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
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify

#######################################################################

def extract_name_href(value):

    # subfunctions copied verbatim from get_page.py
    def strip_html(html):
        txt = ''
        pos = 0
        while True:
            start = html.find('<', pos)
            if start == -1:
                txt += html[pos:]
                break
            txt += html[pos:start]
            stop = html.find('>', start)
            if stop == -1:
                break
            pos = stop+1
            txt += ' '
        return txt.strip()
        
    def extract_hrefs_from_text(page, proto_filter= None):
        """
        extract_hrefs_from_page(page, proto_filter= None) -> <list>
    
        Extract all the href links from the given page text.
        If proto_filter is given, filter out anything that DOES NOT
        match this list of terms.
        Returns the href targets as a list.
        """
        result = []
        lpage = page.lower()
        idx = -1
        while True:
            idx = lpage.find('href=', idx+1)
            if idx == -1:
                break
            idx += len('href=') # maybe +1 ?
            delim = lpage[idx]
            stop = lpage.find(delim, idx+1)
            if stop != -1:
                target = page[idx+1:stop]
                result.append(target)
    
    
        # result now contains ALL hrefs. Filter them
        if proto_filter:
            for pf in proto_filter:
                result = filter(lambda x: x.lower().startswith(pf.lower()), result)
    
        return result


    name = strip_html(value).replace('&quot;', '"')
    hrefs = extract_hrefs_from_text(value)
    if len(hrefs) == 0:
        href = None
    elif len(hrefs) == 1:
        href = hrefs[0]
    else:
        assert False, 'Multiple hrefs in name {value!r}'.format(**locals())
    return name, href


#######################################################################

def fk_handler(obj, fieldname, fk_value, app_label, fk_modelname):
    """
    Set a FK relationship on the model
    """
    fk_model = models.get_model(app_label, fk_modelname)
    assert fk_model is not None, 'ForeignKey model "{fk_modelname}" not found!'.format(**locals())
    slug = slugify(fk_value)
    try:
        fk_obj = fk_model.objects.get(slug=slug)
    except fk_model.DoesNotExist:
        assert False, 'ForeignKey does not exist: model = "{fk_modelname}"; slug = {slug!r}; name = {fk_value!r}'.format(**locals())
        
    setattr(obj, fieldname, fk_obj)
    
    

#######################################################################

def int_pair_handler(obj, fieldname, value_string):
    """
    Handle a pair value.
    """
    value = [ int(e.strip()) for e in value_string.split('-') ]
    assert len(value) == 2, 'The value string {value_string!r} is not a pair'.format(**locals())
    setattr(obj, fieldname, value)

#######################################################################

def float_pair_handler(obj, fieldname, value_string):
    """
    Handle a pair value.
    """
    value = [ float(e.strip()) for e in value_string.split('-') ]
    assert len(value) == 2, 'The value string {value_string!r} is not a pair'.format(**locals())
    setattr(obj, fieldname, value)

#######################################################################

def temperature_pair_handler(obj, fieldname, value_string):
    """
    Handle a pair value.
    """
    p = value_string.find('&#xB0;C')
    if p != -1:
        value_string = value_string[:p]
    value = [ int(e.strip()) for e in value_string.split('-') ]
    assert len(value) == 2, 'The value string {value_string!r} is not a pair'.format(**locals())
    setattr(obj, fieldname, value)

#######################################################################

def size_pair_handler(obj, fieldname, value_string):
    """
    Handle a pair value.
    """
    p = value_string.find('cm')
    if p != -1:
        value_string = value_string[:p]
    value = [ int(e.strip()) for e in value_string.split('-') ]
    assert len(value) == 2, 'The value string {value_string!r} is not a pair'.format(**locals())
    setattr(obj, fieldname, value)

#######################################################################

def hardness_pair_handler(obj, fieldname, value_string):
    """
    Handle a pair value.
    """
    value = [ int(e.strip()) for e in value_string.split('-') ]
    assert len(value) == 2, 'The value string {value_string!r} is not a pair'.format(**locals())
    # convert the value pair from dGH to ppm:
    value = [ int(round(v*1.7848))*10 for v in value ]
    setattr(obj, fieldname, value)

#######################################################################

def basic_handler(obj, fieldname, value):
    """
    Handle a basic value.
    """
    setattr(obj, fieldname, value)
    

#######################################################################

def noop_handler(obj, fieldname, value):
    """
    Handle a value to be ignored.
    """
    return # do nothing
    

#######################################################################

def do_model_values(model, namekey, data_map, data):

    common_name, reference_url = extract_name_href(data[namekey])
    common_name = unicode(common_name, "utf-8", errors="replace")
    slug = slugify(common_name)
    print '{common_name!r}; slug = {slug!r}'.format(**locals())
    dup_count = None
    tmp_slug = slug
    while True:
        try:
            obj, created = model.objects.get_or_create(slug=tmp_slug, 
                                                common_name=common_name)
        except IntegrityError:
            if dup_count is None:
                dup_count = 1
            else:
                dup_count += 1
            tmp_slug = slug + '-{0}'.format(dup_count)
            # and try again
        else:
            break   # created!                  
    for key in data:
        fieldname, handler, args = data_map[key]
        value = data[key].strip()
#         for src, dst in (
#                             ('\xe2\x80\x98', '\u2013'), 
#                             ('\xe2\x80\x9c', '"'),
#                             ('\xe2\x80\x9d', '"'),
#                         ):
#             value = value.replace(src, dst)
        value = unicode(value, "utf-8", errors="replace")
        handler(obj, fieldname, value, *args)
    obj.save()
    print u'{model.__name__}: {obj} saved'.format(**locals())
    print '\t{reference_url}'.format(**locals())


#######################################################################

def do_freshwaterfish(app_label, model, data):
    data_map = {
        'Breeding type': ('breeding_type', fk_handler, (app_label, 'FishBreedingType')),
        'Common name': ('common_name', noop_handler, ()),
        "Fish's latin name":  ('scientific_name', basic_handler, ()),
        'Origin': ('origin', fk_handler, (app_label, 'Origin')),
        'Photo URL': ('photo', noop_handler, ()),
        'Preferred swimming area': ('preferred_area', fk_handler, (app_label, 'FishTankRegion')),
        'Size':  ('size', int_pair_handler, ()),
        "Temperament to it's family": ('temperament_family', fk_handler, (app_label, 'FishTemperament')),
        'Temperament to other species': ('temperament_others', fk_handler, (app_label, 'FishTemperament')),
        'Temperature': ('temperature', temperature_pair_handler, ()),
        'dGH': ('hardness', hardness_pair_handler, ()),
        'ph': ('ph', float_pair_handler, ()),
        }
    do_model_values(model, 'Common name', data_map, data)
    

#######################################################################

def do_freshwaterplant(app_label, model, data):
    data_map = {
        'Growth speed':  ('growth_speed', fk_handler, (app_label, 'PlantGrowthSpeed')),
        'Lighting':  ('lighting', fk_handler, (app_label, 'PlantLighting')),
        'Origin': ('origin', fk_handler, (app_label, 'Origin')),
        'Photo URL': ('photo', noop_handler, ()),
        'Place in the aquarium': ('placement', fk_handler, (app_label, 'PlantTankRegion')),
        'Plant name': ('common_name', noop_handler, ()),
        'Propagation':  ('propagation', fk_handler, (app_label, 'PlantPropagationType')),
        'Size':  ('size', size_pair_handler, ()),
        'Substrate':  ('substrate', fk_handler, (app_label, 'PlantSubstrate')),
        'Temperature': ('temperature', temperature_pair_handler, ()),
        'dGH': ('hardness', hardness_pair_handler, ()),
        'ph': ('ph', float_pair_handler, ()),
         }
    do_model_values(model, 'Plant name', data_map, data)
    

#######################################################################

def do_modelfile(model_filename):

    app_label = os.path.split(os.path.dirname(
                            os.path.dirname(os.path.abspath(__file__))))[-1]

    basename = os.path.split(model_filename)[-1]
    modelname = os.path.splitext(basename)[0]

    #assert modelname in ['FreshwaterFish', 'FreshwaterPlants'], 'can only deal with the two info items'
    
    model = models.get_model(app_label, modelname)
    if model is None:
        print '[!!!] Model "{modelname}" not found!'.format(**locals())
        return

    with open(model_filename) as f:
        records = pickle.load(f)
        for record in records:
            if modelname == 'FreshwaterFish':
                do_freshwaterfish(app_label, model, record)
            elif modelname == 'FreshwaterPlant':
                do_freshwaterplant(app_label, model, record)
            else:
                print '[!!!] cannot deal with Model "{modelname}"'.format(**locals())
                
    

#######################################################################

def main(options, args):
    for arg in args:
        do_modelfile(arg)    

    
#######################################################################

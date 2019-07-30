"""
Views for the aquainfo application
"""
#######################################################################

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import (FishBreedingType, FishTankRegion, FishTemperament,
                     FreshwaterFish, FreshwaterPlant, Origin, PlantGrowthSpeed,
                     PlantLighting, PlantPropagationType, PlantSubstrate,
                     PlantTankRegion)


"""
Automatic model view generator:

for model in sorted(['Origin', 'FishBreedingType', 'PlantPropagationType',
                     'PlantTankRegion', 'FishTankRegion', 'FishTemperament',
                     'PlantGrowthSpeed', 'PlantLighting', 'PlantSubstrate',
                     'FreshwaterFish', 'FreshwaterPlant',
                     ]):
    print '''class {model}Mixin(object):
    queryset = {model}.objects.active()

class {model}ListView({model}Mixin, ListView):
    paginate_by = 50

class {model}DetailView({model}Mixin, DetailView):
    pass

{lowermodel}_list = {model}ListView.as_view()
{lowermodel}_detail = {model}DetailView.as_view()


#######################################################################
'''.format(model=model, lowermodel=model.lower())


Automatic url pattern generator:

for model in sorted(['Origin', 'FishBreedingType', 'PlantPropagationType',
                     'PlantTankRegion', 'FishTankRegion', 'FishTemperament',
                     'PlantGrowthSpeed', 'PlantLighting', 'PlantSubstrate',
                     'FreshwaterFish', 'FreshwaterPlant',
                     ]):
    print '''    # {model} url patterns:
    url(r'^{lowermodel}/$',
        'aquainfo.views.{lowermodel}_list',
        name='aquainfo-{lowermodel}-list',
        ),

    url(r'^{lowermodel}/(?P<slug>[\\w-]+)/$', 
        'aquainfo.views.{lowermodel}_detail',
        name='aquainfo-{lowermodel}-detail',
        ),

'''.format(model=model, lowermodel=model.lower())


"""

class FishBreedingTypeMixin(object):
    queryset = FishBreedingType.objects.active()

class FishBreedingTypeListView(FishBreedingTypeMixin, ListView):
    paginate_by = 50

class FishBreedingTypeDetailView(FishBreedingTypeMixin, DetailView):
    pass

fishbreedingtype_list = FishBreedingTypeListView.as_view()
fishbreedingtype_detail = FishBreedingTypeDetailView.as_view()


#######################################################################

class FishTankRegionMixin(object):
    queryset = FishTankRegion.objects.active()

class FishTankRegionListView(FishTankRegionMixin, ListView):
    paginate_by = 50

class FishTankRegionDetailView(FishTankRegionMixin, DetailView):
    pass

fishtankregion_list = FishTankRegionListView.as_view()
fishtankregion_detail = FishTankRegionDetailView.as_view()


#######################################################################

class FishTemperamentMixin(object):
    queryset = FishTemperament.objects.active()

class FishTemperamentListView(FishTemperamentMixin, ListView):
    paginate_by = 50

class FishTemperamentDetailView(FishTemperamentMixin, DetailView):
    pass

fishtemperament_list = FishTemperamentListView.as_view()
fishtemperament_detail = FishTemperamentDetailView.as_view()


#######################################################################

class FreshwaterFishMixin(object):
    queryset = FreshwaterFish.objects.active()

class FreshwaterFishListView(FreshwaterFishMixin, ListView):
    paginate_by = 50

class FreshwaterFishDetailView(FreshwaterFishMixin, DetailView):
    pass

freshwaterfish_list = FreshwaterFishListView.as_view()
freshwaterfish_detail = FreshwaterFishDetailView.as_view()


#######################################################################

class FreshwaterPlantMixin(object):
    queryset = FreshwaterPlant.objects.active()

class FreshwaterPlantListView(FreshwaterPlantMixin, ListView):
    paginate_by = 50

class FreshwaterPlantDetailView(FreshwaterPlantMixin, DetailView):
    pass

freshwaterplant_list = FreshwaterPlantListView.as_view()
freshwaterplant_detail = FreshwaterPlantDetailView.as_view()


#######################################################################

class OriginMixin(object):
    queryset = Origin.objects.active()

class OriginListView(OriginMixin, ListView):
    paginate_by = 50

class OriginDetailView(OriginMixin, DetailView):
    pass

origin_list = OriginListView.as_view()
origin_detail = OriginDetailView.as_view()


#######################################################################

class PlantGrowthSpeedMixin(object):
    queryset = PlantGrowthSpeed.objects.active()

class PlantGrowthSpeedListView(PlantGrowthSpeedMixin, ListView):
    paginate_by = 50

class PlantGrowthSpeedDetailView(PlantGrowthSpeedMixin, DetailView):
    pass

plantgrowthspeed_list = PlantGrowthSpeedListView.as_view()
plantgrowthspeed_detail = PlantGrowthSpeedDetailView.as_view()


#######################################################################

class PlantLightingMixin(object):
    queryset = PlantLighting.objects.active()

class PlantLightingListView(PlantLightingMixin, ListView):
    paginate_by = 50

class PlantLightingDetailView(PlantLightingMixin, DetailView):
    pass

plantlighting_list = PlantLightingListView.as_view()
plantlighting_detail = PlantLightingDetailView.as_view()


#######################################################################

class PlantPropagationTypeMixin(object):
    queryset = PlantPropagationType.objects.active()

class PlantPropagationTypeListView(PlantPropagationTypeMixin, ListView):
    paginate_by = 50

class PlantPropagationTypeDetailView(PlantPropagationTypeMixin, DetailView):
    pass

plantpropagationtype_list = PlantPropagationTypeListView.as_view()
plantpropagationtype_detail = PlantPropagationTypeDetailView.as_view()


#######################################################################

class PlantSubstrateMixin(object):
    queryset = PlantSubstrate.objects.active()

class PlantSubstrateListView(PlantSubstrateMixin, ListView):
    paginate_by = 50

class PlantSubstrateDetailView(PlantSubstrateMixin, DetailView):
    pass

plantsubstrate_list = PlantSubstrateListView.as_view()
plantsubstrate_detail = PlantSubstrateDetailView.as_view()


#######################################################################

class PlantTankRegionMixin(object):
    queryset = PlantTankRegion.objects.active()

class PlantTankRegionListView(PlantTankRegionMixin, ListView):
    paginate_by = 50

class PlantTankRegionDetailView(PlantTankRegionMixin, DetailView):
    pass

planttankregion_list = PlantTankRegionListView.as_view()
planttankregion_detail = PlantTankRegionDetailView.as_view()


#######################################################################
#######################################################################
#######################################################################

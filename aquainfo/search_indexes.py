"""
Haystack search indexes for aquainfo application.
"""
###############################################################

from haystack import indexes

from .models import (FishBreedingType, FishTankRegion, FishTemperament,
                     FreshwaterFish, FreshwaterPlant, Origin, PlantGrowthSpeed,
                     PlantLighting, PlantPropagationType, PlantSubstrate,
                     PlantTankRegion)

###############################################################

# site.register(FishBreedingType)
# site.register(FishTankRegion)
# site.register(FishTemperament)
# site.register(FreshwaterFish)
# site.register(FreshwaterPlant)
# site.register(Origin)
# site.register(PlantGrowthSpeed)
# site.register(PlantLighting)
# site.register(PlantPropagationType)
# site.register(PlantSubstrate)
# site.register(PlantTankRegion)

class AquainfoBaseIndex(indexes.SearchIndex):
    model = None
    text = indexes.CharField(document=True, use_template=True)


    def get_model(self, using=None):
        return self.model


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.active()


###############################################################

class FreshwaterFishIndex(AquainfoBaseIndex, indexes.Indexable):
    model = FreshwaterFish

class FreshwaterPlantIndex(AquainfoBaseIndex, indexes.Indexable):
    model = FreshwaterPlant

###############################################################

# class Page_Index(indexes.SearchIndex):
#     text = indexes.CharField(document=True, use_template=True)
#     pub_date = indexes.DateTimeField(model_attr='modified')
#     title = indexes.CharField(model_attr='title', boost=4.0)
# 
#     def index_queryset(self):
#         """Used when the entire index for model is updated."""
#         return Page.objects.filter(active=True, public=True)
# 
#     def prepare(self, obj):
#         """
#         Do document boosting.
#         """
#         data = super(self.__class__, self).prepare(obj)
#         data['boost'] = 3.0
#         return data
# 
# 
# site.register(Page, Page_Index)

###############################################################

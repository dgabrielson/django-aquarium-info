"""
The url patterns for the aquainfo application.
"""

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='aquainfo/index.html'),
        name='aquainfo-landing',
        ),
    # FishBreedingType url patterns:
    url(r'^fishbreedingtype/$', 
        views.fishbreedingtype_list, 
        name='aquainfo-fishbreedingtype-list',
        ),
    url(r'^fishbreedingtype/(?P<slug>[\w-]+)/$', 
        views.fishbreedingtype_detail, 
        name='aquainfo-fishbreedingtype-detail',
        ),
    # FishTankRegion url patterns:
    url(r'^fishtankregion/$', 
        views.fishtankregion_list, 
        name='aquainfo-fishtankregion-list',
        ),
    url(r'^fishtankregion/(?P<slug>[\w-]+)/$', 
        views.fishtankregion_detail, 
        name='aquainfo-fishtankregion-detail',
        ),
    # FishTemperament url patterns:
    url(r'^fishtemperament/$', 
        views.fishtemperament_list, 
        name='aquainfo-fishtemperament-list',
        ),
    url(r'^fishtemperament/(?P<slug>[\w-]+)/$', 
        views.fishtemperament_detail, 
        name='aquainfo-fishtemperament-detail',
        ),
    # FreshwaterFish url patterns:
    url(r'^freshwaterfish/$', 
        views.freshwaterfish_list, 
        name='aquainfo-freshwaterfish-list',
        ),
    url(r'^freshwaterfish/(?P<slug>[\w-]+)/$', 
        views.freshwaterfish_detail, 
        name='aquainfo-freshwaterfish-detail',
        ),
    # FreshwaterPlant url patterns:
    url(r'^freshwaterplant/$', 
        views.freshwaterplant_list, 
        name='aquainfo-freshwaterplant-list',
        ),
    url(r'^freshwaterplant/(?P<slug>[\w-]+)/$', 
        views.freshwaterplant_detail, 
        name='aquainfo-freshwaterplant-detail',
        ),
    # Origin url patterns:
    url(r'^origin/$', 
        views.origin_list, 
        name='aquainfo-origin-list',
        ),
    url(r'^origin/(?P<slug>[\w-]+)/$', 
        views.origin_detail, 
        name='aquainfo-origin-detail',
        ),
    # PlantGrowthSpeed url patterns:
    url(r'^plantgrowthspeed/$', 
        views.plantgrowthspeed_list, 
        name='aquainfo-plantgrowthspeed-list',
        ),
    url(r'^plantgrowthspeed/(?P<slug>[\w-]+)/$', 
        views.plantgrowthspeed_detail, 
        name='aquainfo-plantgrowthspeed-detail',
        ),
    # PlantLighting url patterns:
    url(r'^plantlighting/$', 
        views.plantlighting_list, 
        name='aquainfo-plantlighting-list',
        ),
    url(r'^plantlighting/(?P<slug>[\w-]+)/$', 
        views.plantlighting_detail, 
        name='aquainfo-plantlighting-detail',
        ),
    # PlantPropagationType url patterns:
    url(r'^plantpropagationtype/$', 
        views.plantpropagationtype_list, 
        name='aquainfo-plantpropagationtype-list',
        ),
    url(r'^plantpropagationtype/(?P<slug>[\w-]+)/$', 
        views.plantpropagationtype_detail, 
        name='aquainfo-plantpropagationtype-detail',
        ),
    # PlantSubstrate url patterns:
    url(r'^plantsubstrate/$', 
        views.plantsubstrate_list, 
        name='aquainfo-plantsubstrate-list',
        ),
    url(r'^plantsubstrate/(?P<slug>[\w-]+)/$', 
        views.plantsubstrate_detail, 
        name='aquainfo-plantsubstrate-detail',
        ),
    # PlantTankRegion url patterns:
    url(r'^planttankregion/$', 
        views.planttankregion_list, 
        name='aquainfo-planttankregion-list',
        ),
    url(r'^planttankregion/(?P<slug>[\w-]+)/$', 
        views.planttankregion_detail, 
        name='aquainfo-planttankregion-detail',
        ),
    ]

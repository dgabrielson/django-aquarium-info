"""
Admin classes for the budget application
"""
#######################################################################

from django.contrib import admin

from .models import (FishBreedingType, FishTankRegion, FishTemperament,
                     FreshwaterFish, FreshwaterPlant, Origin, PlantGrowthSpeed,
                     PlantLighting, PlantPropagationType, PlantSubstrate,
                     PlantTankRegion)

#######################################################################

class TypeBaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'active', ]
    list_filter = ['active', 'modified', 'created', ]
    prepopulated_fields = {'slug': ("name",)}
    save_on_top = True


admin.site.register(Origin, TypeBaseAdmin)
admin.site.register(FishBreedingType, TypeBaseAdmin)
admin.site.register(PlantPropagationType, TypeBaseAdmin)

admin.site.register(PlantTankRegion, TypeBaseAdmin)
admin.site.register(FishTankRegion, TypeBaseAdmin)
admin.site.register(FishTemperament, TypeBaseAdmin)

admin.site.register(PlantGrowthSpeed, TypeBaseAdmin)
admin.site.register(PlantLighting, TypeBaseAdmin)
admin.site.register(PlantSubstrate, TypeBaseAdmin)

#######################################################################


class ItemInfoBaseAdmin(admin.ModelAdmin):
    list_display = ['common_name', 'slug', 'active', ]
    list_filter = ['active', 'modified', 'created', ]
    prepopulated_fields = {'slug': ("common_name",)}
    save_on_top = True
    search_fields = ['common_name', 'scientific_name']


admin.site.register(FreshwaterFish, ItemInfoBaseAdmin)
admin.site.register(FreshwaterPlant, ItemInfoBaseAdmin)

#######################################################################

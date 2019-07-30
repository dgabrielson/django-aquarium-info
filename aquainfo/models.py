"""
Models for the aquainfo application.
"""
#######################################################################

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

#######################################################################
#######################################################################
#######################################################################

class CustomQuerySet(models.query.QuerySet):
    """
    Custom QuerySet.
    """
    def active(self):
        """
        Returns only the active items in this queryset
        """
        return self.filter(active=True)


#######################################################################

class CustomQuerySetManager(models.Manager):
    """
    Custom Manager for an arbitrary model, just a wrapper for returning
    a custom QuerySet
    """
    use_for_related_fields = False
    queryset_class = models.query.QuerySet

    def get_queryset(self):
        """
        Return the custom QuerySet
        """
        return self.queryset_class(self.model)



#######################################################################

class AquainfoBaseModel(models.Model):
    """
    An abstract base class.
    """
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False,
                                   verbose_name='creation time')
    modified = models.DateTimeField(auto_now=True, editable=False,
                                    verbose_name='last modification time')


    class Meta:
        abstract = True



    def get_list_url(self):
        return reverse('aquainfo-{0}-list'.format(self.__class__.__name__.lower()))


    def get_absolute_url(self):
        return reverse('aquainfo-{0}-detail'.format(self.__class__.__name__.lower()),
                        kwargs={'slug': self.slug})




#######################################################################
#######################################################################
#######################################################################

class TypeMixin(models.Model):
    """
    For the variety of types.
    """
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    description = models.TextField(blank=True)


    class Meta:
        abstract = True
        ordering = ['name', ]


    def __unicode__(self):
        return self.name



#######################################################################
#######################################################################
#######################################################################

class Origin(AquainfoBaseModel, TypeMixin):
    """
    Where things are from.
    """
    objects = CustomQuerySet.as_manager()



#######################################################################
#######################################################################
#######################################################################

class FishBreedingType(AquainfoBaseModel, TypeMixin):
    """
    How animals reproduce.
    """
    objects = CustomQuerySet.as_manager()


#######################################################################
#######################################################################
#######################################################################

class PlantPropagationType(AquainfoBaseModel, TypeMixin):
    """
    How plants reproduce.
    """
    objects = CustomQuerySet.as_manager()



#######################################################################
#######################################################################
#######################################################################

class PlantTankRegion(AquainfoBaseModel, TypeMixin):
    """
    Where plants should be in a tank.
    """
    objects = CustomQuerySet.as_manager()



#######################################################################
#######################################################################
#######################################################################

class FishTankRegion(AquainfoBaseModel, TypeMixin):
    """
    Where fish like to be in a tank.
    """
    objects = CustomQuerySet.as_manager()


#######################################################################
#######################################################################
#######################################################################

class FishTemperament(AquainfoBaseModel, TypeMixin):
    """
    Where fish like to be in a tank.
    """
    objects = CustomQuerySet.as_manager()


#######################################################################
#######################################################################
#######################################################################

class PlantGrowthSpeed(AquainfoBaseModel, TypeMixin):
    """
    How fast plants grow.
    """
    objects = CustomQuerySet.as_manager()


#######################################################################
#######################################################################
#######################################################################

class PlantLighting(AquainfoBaseModel, TypeMixin):
    """
    What kind of PlantLighting plants like.
    """
    objects = CustomQuerySet.as_manager()

    class Meta:
        verbose_name_plural = 'plant lighting'


#######################################################################
#######################################################################
#######################################################################

class PlantSubstrate(AquainfoBaseModel, TypeMixin):
    """
    What kind of PlantSubstrate plants like
    """
    objects = CustomQuerySet.as_manager()


#######################################################################
#######################################################################
#######################################################################

class InfoItemQuerySet(CustomQuerySet):
    """
    Provide a custom model API.  Urls, views, etc. should only
    use these methods, never .filter(...).
    """


#################################################

class InfoItem(AquainfoBaseModel):
    """
    A further base class -- common elements of both Fish and Plant models.
    """
    common_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)
    scientific_name = models.CharField(max_length=128, blank=True)
    origin = models.ForeignKey(Origin, limit_choices_to={'active': True},
                               null=True, blank=True, on_delete=models.SET_NULL)
    size_min = models.PositiveSmallIntegerField(null=True, blank=True,
                                                verbose_name='minimum size',
                                                help_text='in centimeters (cm)')
    size_max = models.PositiveSmallIntegerField(null=True, blank=True,
                                                verbose_name='maximum size',
                                                help_text='in centimeters (cm)')


    objects = InfoItemQuerySet.as_manager()


    class Meta:
        abstract = True
        ordering = ('common_name', )


    def __unicode__(self):
        return self.common_name



    def get_absolute_url(self):
        """
        So this is a nice little bit of generic magic as long as the
        named url 'aquainfo-modelname-detail' exists.
        """
        return reverse('aquainfo-{self.__class__.__name__}-detail'.format(
                    self=self).lower(), kwargs={'slug': self.slug})


    @property
    def size(self):
        """
        Return the property as a tuple.
        """
        return (self.size_min, self.size_max)

    @size.setter
    def size(self, value):
        """
        Set the property from a pair
        """
        self.size_min, self.size_max = value


    def size_display(self):
        """
        Return a string for the size range
        """
        result = u''
        if self.size_min is not None:
            result += '{self.size_min}'.format(self=self)
            if self.size_max is not None:
                result += '&ndash;'
        if self.size_max is not None:
            result += '{self.size_max}'.format(self=self)
        return mark_safe(result)
    size_display.allow_tags=True


    def clean(self, *args, **kwargs):
        """
        Sanity check
        """
        result = super(InfoItem, self).clean()
        if self.size_min is not None and self.size_max is not None:
            if self.size_min > self.size_max:
                raise ValidationError('minimum size cannot be larger than maximum size')
        return result


#######################################################################
#######################################################################
#######################################################################

class FreshwaterMixin(models.Model):
    """
    Common fields for freshwater.
    ph, temperature, hardness
    """
    ph_min = models.FloatField(null=True, blank=True, verbose_name='minimum pH')
    ph_max = models.FloatField(null=True, blank=True, verbose_name='maximum pH')
    temperature_min = models.PositiveSmallIntegerField(null=True, blank=True,
                                            verbose_name='minimum temperature',
                                            help_text='in degrees Celcius')
    temperature_max = models.PositiveSmallIntegerField(null=True, blank=True,
                                            verbose_name='maximum temperature',
                                            help_text='in degrees Celcius')
    hardness_min = models.PositiveSmallIntegerField(null=True, blank=True,
                                        verbose_name='minimum hardness',
                                        help_text='in parts per million (ppm)')
    hardness_max = models.PositiveSmallIntegerField(null=True, blank=True,
                                        verbose_name='maximum hardness',
                                        help_text='in parts per million (ppm)')


    class Meta:
        abstract = True


    @property
    def ph(self):
        """
        Return the property as a tuple.
        """
        return (self.ph_min, self.ph_max)

    @ph.setter
    def ph(self, value):
        """
        Set the property from a pair
        """
        self.ph_min, self.ph_max = value

    def ph_display(self):
        """
        Return a string for the size range
        """
        result = u''
        if self.ph_min is not None:
            result += '{self.ph_min:.1f}'.format(self=self)
            if self.ph_max is not None:
                result += '&ndash;'
        if self.ph_max is not None:
            result += '{self.ph_max:.1f}'.format(self=self)
        return mark_safe(result)
    ph_display.allow_tags=True



    @property
    def temperature(self):
        """
        Return the property as a tuple.
        """
        return (self.temperature_min, self.temperature_max)

    @temperature.setter
    def temperature(self, value):
        """
        Set the property from a pair
        """
        self.temperature_min, self.temperature_max = value

    def temperature_display(self):
        """
        Return a string for the size range
        """
        result = u''
        if self.temperature_min is not None:
            result += '{self.temperature_min}'.format(self=self)
            if self.temperature_max is not None:
                result += '&ndash;'
        if self.ph_max is not None:
            result += '{self.temperature_max}'.format(self=self)
        return mark_safe(result)
    temperature_display.allow_tags=True



    @property
    def hardness(self):
        """
        Return the property as a tuple.
        """
        return (self.hardness_min, self.hardness_max)

    @hardness.setter
    def hardness(self, value):
        """
        Set the property from a pair
        """
        self.hardness_min, self.hardness_max = value

    def hardness_display(self):
        """
        Return a string for the size range
        """
        result = u''
        if self.hardness_min is not None:
            result += '{self.hardness_min}'.format(self=self)
            if self.hardness_max is not None:
                result += '&ndash;'
        if self.hardness_max is not None:
            result += '{self.hardness_max}'.format(self=self)
        return mark_safe(result)
    temperature_display.allow_tags=True



    def clean(self, *args, **kwargs):
        """
        Sanity check
        """
        result = super(FreshwaterMixin, self).clean()
        if self.ph_min is not None and self.ph_max is not None:
            if self.ph_min > self.ph_max:
                raise ValidationError('minimum ph cannot be larger than maximum ph')
        if self.temperature_min is not None and self.temperature_max is not None:
            if self.temperature_min > self.temperature_max:
                raise ValidationError('minimum temperature cannot be larger than maximum temperature')
        if self.hardness_min is not None and self.hardness_max is not None:
            if self.hardness_min > self.hardness_max:
                raise ValidationError('minimum hardness cannot be larger than maximum hardness')
        return result



#######################################################################
#######################################################################
#######################################################################

class FreshwaterFish(InfoItem, FreshwaterMixin):
    """
    All the info, freshwater, plus fish foreign keys
    """
    breeding_type = models.ForeignKey(FishBreedingType, null=True, blank=True,
                                      limit_choices_to={'active': True},
                                      on_delete=models.SET_NULL)
    preferred_area = models.ForeignKey(FishTankRegion, null=True, blank=True,
                                       limit_choices_to={'active': True},
                                       on_delete=models.SET_NULL)
    temperament_family = models.ForeignKey(FishTemperament, null=True,
                                    blank=True,
                                    limit_choices_to={'active': True},
                                    related_name='fishtemperament_family_set',
                                    on_delete=models.SET_NULL)
    temperament_others = models.ForeignKey(FishTemperament, null=True,
                                    blank=True,
                                    limit_choices_to={'active': True},
                                    related_name='fishtemperament_others_set',
                                    on_delete=models.SET_NULL)


    objects = CustomQuerySet.as_manager()


    class Meta:
        verbose_name_plural = 'freshwater fish'
        ordering = ('common_name', )


#######################################################################
#######################################################################
#######################################################################

class FreshwaterPlant(InfoItem, FreshwaterMixin):
    """
    All the info, freshwater, plus plant foreign keys
    """
    growth_speed = models.ForeignKey(PlantGrowthSpeed, null=True, blank=True,
                                      limit_choices_to={'active': True},
                                      on_delete=models.SET_NULL)
    lighting = models.ForeignKey(PlantLighting, null=True, blank=True,
                                 limit_choices_to={'active': True},
                                 on_delete=models.SET_NULL)
    placement = models.ForeignKey(PlantTankRegion, null=True, blank=True,
                                  limit_choices_to={'active': True},
                                  on_delete=models.SET_NULL)
    propagation = models.ForeignKey(PlantPropagationType, null=True, blank=True,
                                    limit_choices_to={'active': True},
                                    on_delete=models.SET_NULL)
    substrate = models.ForeignKey(PlantSubstrate, null=True, blank=True,
                                  limit_choices_to={'active': True},
                                  on_delete=models.SET_NULL)


    objects = CustomQuerySet.as_manager()


#######################################################################
#######################################################################
#######################################################################

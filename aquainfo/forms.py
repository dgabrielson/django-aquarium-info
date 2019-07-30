"""
Forms for the aquainfo application.
"""
#######################################################################

from django import forms

from .models import AquainfoModel

#######################################################################

class SplitMinMaxWidget(forms.MultiWidget):
    """
    A Widget that splits input into two <input type="text"> boxes.
    """

    def __init__(self, attrs=None):
        widgets = (form.TextInput(attrs=attrs, format=date_format),
                   form.TextInput(attrs=attrs, format=time_format))
        super(self.__class__, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value 
        return [None, None]

#######################################################################
#######################################################################
#######################################################################

class SplitMinMaxField(forms.MultiValueField):
    
    def __init__(self, *args, **kwargs):
        fields = (forms.IntegerField, forms.IntegerField)
        return super(self.__class__, self).__init__(fields, *args, **kwargs)
        

#######################################################################
#######################################################################
#######################################################################

# class AquainfoModelForm(forms.ModelForm):
#     """
#     Form for the model.
#     """
#     class Meta:
#         model = AquainfoModel
#         exclude = ['active', ]
#         #widgets = {
#         #    }
    
    
#######################################################################
#######################################################################
#######################################################################

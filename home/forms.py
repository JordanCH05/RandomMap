from django import forms

from .models import Map


class MapForm(forms.ModelForm):
    
    class Meta:
        model = Map
        fields = [
            'latitude',
            'longitude',
            'no_of_dests',
            'distance',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['latitude'].widget.attrs['placeholder'] = 51.5078
        self.fields['longitude'].widget.attrs['placeholder'] = -0.1279
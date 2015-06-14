from django.utils.translation import ugettext as _
from django import forms


class FormWithCoordinates(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormWithCoordinates, self).__init__(*args, **kwargs)
        self.fields['lat'].widget = forms.HiddenInput()
        self.fields['lng'].widget = forms.HiddenInput()

    def clean(self):
        cleaned_data = super(FormWithCoordinates, self).clean()
        lat = cleaned_data.get("lat")
        lng = cleaned_data.get("lng")

        if not lat or not lng:
            raise forms.ValidationError(_("You must provide a location."))

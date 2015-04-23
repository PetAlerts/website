from django import forms
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Alert


class Home(TemplateView):
    template_name = 'coming-soon.html'


class AlertDetailView(DetailView):
    model = Alert


class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['lat'].widget = forms.HiddenInput()
        self.fields['lng'].widget = forms.HiddenInput()


class AlertCreateView(CreateView):
    model = Alert
    form_class = AlertForm
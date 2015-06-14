from django import forms
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from petalerts.forms import FormWithCoordinates
from .models import Alert


class Home(TemplateView):
    template_name = 'home.html'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(Home, cls).as_view(**initkwargs)
        return login_required(view)


class AlertDetailView(DetailView):
    model = Alert


class AlertForm(FormWithCoordinates):
    class Meta:
        model = Alert
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AlertForm, self).__init__(*args, **kwargs)
        self.fields['details'].widget = forms.Textarea()


class AlertCreateView(CreateView):
    model = Alert
    form_class = AlertForm


class AlertList(ListView):
    template_name = "alerts/alert_list.html"
    model = Alert
    paginate_by = 6
    ordering = ['-date']

    def get_queryset(self):
        species = self.request.GET.get('species')
        q = super(AlertList, self).get_queryset()
        if species is not None:
            return q.filter(species=species)
        return q

    def get_context_data(self, **kwargs):
        context = super(AlertList, self).get_context_data()
        context['species'] = Alert.SPECIES_CHOICES
        return context

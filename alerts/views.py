from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import Alert


class Home(TemplateView):
    template_name = 'coming-soon.html'


class AlertDetailView(DetailView):
    model = Alert

from django import forms
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, render
from .models import Alert


class Home(TemplateView):
    template_name = 'coming-soon.html'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(Home, cls).as_view(**initkwargs)
        return login_required(view)

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
        self.fields['details'].widget = forms.Textarea()

    def clean(self):
        cleaned_data = super(AlertForm, self).clean()
        lat = cleaned_data.get("lat")
        lng = cleaned_data.get("lng")

        if not lat or not lng:
            raise forms.ValidationError(_("You must provide the pet's location."))


class AlertCreateView(CreateView):
    model = Alert
    form_class = AlertForm


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.is_active = False
            new_user.save()
            return home(request)
    return render_to_response(
        'registration/signup.html',
        RequestContext(
            request,
            {
                'form': form,
            }
        )
    )

def login(request):
    return render(request, 'registration/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

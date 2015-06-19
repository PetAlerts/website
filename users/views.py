from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from petalerts.forms import FormWithCoordinates
from .models import AreaSubscription


class Login(TemplateView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('alerts:home')
        return super(Login, self).dispatch(request, *args, **kwargs)


def logout(request):
    auth_logout(request)
    return redirect('/')


class UserSubscriptionsList(ListView):
    model = AreaSubscription
    template_name = 'users/subscriptions_list.html'

    def get_queryset(self):
        q = super(UserSubscriptionsList, self).get_queryset()
        return q.filter(user=self.request.user)


class SubscriptionForm(FormWithCoordinates):
    class Meta:
        model = AreaSubscription
        fields = ['lat', 'lng', 'radius_km']

    def __init__(self, user, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.instance.user = user


class UserSubscriptionsCreate(CreateView):
    template_name = 'users/subscription_form.html'
    form_class = SubscriptionForm

    def get_form_kwargs(self):
        kwargs = super(UserSubscriptionsCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

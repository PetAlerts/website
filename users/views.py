from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.shortcuts import redirect


class Login(TemplateView):
    template_name = 'registration/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('alerts:home')
        return super(Login, self).dispatch(request, *args, **kwargs)


def logout(request):
    auth_logout(request)
    return redirect('/')
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.urls import reverse


def home(request):
    if request.user.is_authenticated:
        return redirect(reverse('projects:project_list'))
    else:
        return render(request, 'home.html')


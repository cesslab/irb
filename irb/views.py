from django.views.generic import TemplateView
from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        redirect('projects:project_list')
    else:
        render(request, 'home.html')


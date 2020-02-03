from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse_lazy('projects:project_list'))

    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('projects:project_list'))
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse_lazy('home'))

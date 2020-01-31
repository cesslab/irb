from django.urls import path

from .views import SignUp, login_user, logout_user

app_name = 'accounts'

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
]

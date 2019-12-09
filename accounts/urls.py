from django.urls import path

from .views import SignUp

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup')
]

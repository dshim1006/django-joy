from django.urls import path

from . import views


# TODO: add profile & password reset url
urlpatterns = [
    path('login/', views.LogIn.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]
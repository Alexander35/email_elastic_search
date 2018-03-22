from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='main/')),
    path('main/', views.main, name='main'),
    path('new_mails_list', views.new_mails_list, name='new_mails_list'),
]
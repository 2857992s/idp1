from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('support', views.support, name='support'),
    path('about', views.about, name='about'),
    path('donations', views.donations, name='donations'),
    path('donations_success', views.donations_success, name='donations_success'),
    path('submit-donation/', views.submit_donation, name='submit_donation'),
    path('adoption', views.adoption, name='adoption'),

]
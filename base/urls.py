from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('children/', views.child_list, name='child_list'),
    path('donate/', views.donation_form, name='donation_form'),
    path('donations_success/', views.donation_success, name='donations_sucess'),
    path('adopt/<int:child_id>/', views.adoption_request, name='adoption_request'),
    path('adoption-requests/', views.adoption_requests_view, name='adoption_requests'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]





   

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('services/', views.services, name='services'),
     path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('products/', views.products, name='products'),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Add your URL patterns here, for example:
    # path('login/', views.login_view, name='login'),
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
]

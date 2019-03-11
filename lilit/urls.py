from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='lilithome'),
    path('cv/', views.cv, name='lilitcv')
]
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('add/', views.add_translation, name='add_translation'),
]



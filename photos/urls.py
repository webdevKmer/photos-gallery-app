from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [

    path('', views.gallery, name='gallery'),
    path('photo/view/<str:pk>', views.view_photo, name='view'),
    path('photo/add/', views.add_photo, name='add'),
    
]

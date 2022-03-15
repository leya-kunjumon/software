from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('software', views.software, name='software'),

    

    #***************************** Manager ******************************

    # path('manager_Dashboard',views.manager_Dashboard),
    
]

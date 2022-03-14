from app import views
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),

#***********************developer***********************************************

    path('developer_Dashboard', views.developer_Dashboard, name='developer_Dashboard'),


    

    #***************************** Manager ******************************

    path('manager_Dashboard',views.manager_Dashboard),

    
]

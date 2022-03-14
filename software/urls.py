from app import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index', views.index, name='index'),
    path('developer_Dashboard',views.developer_Dashboard, name='developer_Dashboard'),
    
]

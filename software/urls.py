from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),


    

    #***************************** Manager ******************************

    path('manager_Dashboard',views.manager_Dashboard),
   
   ############################# TESTER ################################
   
   path('tester_dashboard', views.tester_dashboard, name='tester_dashboard'), 
   path('tester_task', views.tester_task, name='tester_task'), 
   path('tester_taskassigned', views.tester_taskassigned,name='tester_taskassigned'),
   path('tester_taskpending', views.tester_taskpending,name='tester_taskpending'),
   path('tester_projects', views.tester_projects, name='tester_projects'),
   path('tester_projectdetails', views.tester_projectdetails,name='tester_projectdetails'),
   
   
   
   

   
]

from app import views
from django.contrib import admin
from django.urls import path
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),

#***********************developer***********************************************

    path('developer_Dashboard/', views.developer_Dashboard, name='developer_Dashboard'),
    path('developer_task/', views.developer_task, name='developer_task'),
    path('developer_task_form/', views.developer_task_form, name='developer_task_form'),
    path('developer_project/', views.developer_project, name='developer_project'),
    path('developer_project_table/', views.developer_project_table, name='developer_project_table'),
    path('developer_attendance/', views.developer_attendance, name='developer_attendance'),
    path('developer_attendance_list/', views.developer_attendance_list, name='developer_attendance_list'),
    path('developer_reportedissue/', views.developer_reportedissue, name='developer_reportedissue'),
    path('developer_reportedissues/', views.developer_reportedissues, name='developer_reportedissues'),
    path('developer_reportissue/', views.developer_reportissue, name='developer_reportissue'),

    path('developer_applyleave/', views.developer_applyleave, name='developer_applyleave'),
    path('developer_apply_leave/', views.developer_apply_leave, name='developer_apply_leave'),    
    path('developer_apply_leave_list/', views.developer_apply_leave_list, name='developer_apply_leave_list'),

    path('developer_account_settings/', views.developer_account_settings, name='developer_account_settings'),
    path('developer_change_password/', views.developer_change_password, name='developer_change_password'),

    

    #***************************** Manager ******************************

    path('manager_Dashboard',views.manager_Dashboard),

    
]

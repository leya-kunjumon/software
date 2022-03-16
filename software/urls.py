from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('', views.index, name='index'),
    path('software', views.software, name='software'),

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

    #**************************** TESTER ********************************
  
    path('tester_dashboard', views.tester_dashboard, name='tester_dashboard'), 
    path('tester_task', views.tester_task, name='tester_task'), 
    path('tester_taskassigned', views.tester_taskassigned,name='tester_taskassigned'),
    path('tester_taskpending', views.tester_taskpending,name='tester_taskpending'),
    path('tester_projects', views.tester_projects, name='tester_projects'),
    path('tester_projectdetails', views.tester_projectdetails,name='tester_projectdetails'),

    #***************************** Project Manager ******************************

    path('pm_Dashboard', views.pm_Dashboard, name='pm_Dashboard'),
    path('pm_projects', views.pm_projects, name='pm_projects'),
    path('pm_upcomingProject', views.pm_upcomingProject, name='pm_upcomingProject'),
    path('pm_currentProject', views.pm_currentProject, name='pm_currentProject'),
    path('pm_completedProject', views.pm_completedProject, name='pm_completedProject'),
    path('pm_createProject', views.pm_createProject, name='pm_createProject'),
    path('pm_newProj_status', views.pm_newProj_status, name='pm_newProj_status'),
    path('pm_assignProject', views.pm_assignProject, name='pm_assignProject'),
    path('pm_newProject', views.pm_newProject, name='pm_newProject'),
    path('pm_acceptedProject', views.pm_acceptedProject, name='pm_acceptedProject'),
    path('pm_rejectedProject', views.pm_rejectedProject, name='pm_rejectedProject'),
    path('pm_currentProjectFirst', views.pm_currentProjectFirst, name='pm_currentProjectFirst'),
    path('pm_currentprojectTeam', views.pm_currentprojectTeam, name='pm_currentprojectTeam'),
    path('pm_currentprojectTeamList', views.pm_currentprojectTeamList, name='pm_currentprojectTeamList'),
    path('pm_completedFirst', views.pm_completedFirst, name='pm_completedFirst'),
    path('pm_completeProj_Team', views.pm_completeProj_Team, name='pm_completeProj_Team'),
    path('pm_completeProj_Teamlist', views.pm_completeProj_Teamlist, name='pm_completeProj_Teamlist'),
    path('pm_employee', views.pm_employee, name='pm_employee'),
    path('pm_employee_TL', views.pm_employee_TL, name='pm_employee_TL'),
    path('pm_employee_developer', views.pm_employee_developer, name='pm_employee_developer'),
    path('pm_emp_developers_dashboard', views.pm_emp_developers_dashboard, name='pm_emp_developers_dashboard'),
    path('pm_developer_team', views.pm_developer_team, name='pm_developer_team'),
    path('pm_TL_Team', views.pm_TL_Team, name='pm_TL_Team'),
    path('pm_TL_Team_profile', views.pm_TL_Team_profile, name='pm_TL_Team_profile'),
    path('pm_TL_Team_involved', views.pm_TL_Team_involved, name='pm_TL_Team_involved'),
    path('pm_TL_Team_attendence', views.pm_TL_Team_attendence, name='pm_TL_Team_attendence'),
    path('pm_TL_Team_viewAttendence', views.pm_TL_Team_viewAttendence, name='pm_TL_Team_viewAttendence'),
    path('pm_tl_dashboard', views.pm_tl_dashboard, name='pm_tl_dashboard'),
    path('pm_reportedIssues', views.pm_reportedIssues, name='pm_reportedIssues'),
    path('pm_report_reportedIssue', views.pm_report_reportedIssue, name='pm_report_reportedIssue'),
    path('pm_reportedIssue_action', views.pm_reportedIssue_action, name='pm_reportedIssue_action'),
    path('pm_report_issue', views.pm_report_issue, name='pm_report_issue'),
    path('pm_tl_reported_issues', views.pm_tl_reported_issues, name='pm_tl_reported_issues'),
    path('pm_tl_issuesVerified', views.pm_tl_issuesVerified, name='pm_tl_issuesVerified'),
    path('pm_applyLeave', views.pm_applyLeave, name='pm_applyLeave'),
    path('pm_applyleave_Form', views.pm_applyleave_Form, name='pm_applyleave_Form'),
    path('pm_requested_leave', views.pm_requested_leave, name='pm_requested_leave'),
    path('pm_Attendence', views.pm_Attendence, name='pm_Attendence'),
    path('pm_attendenceList', views.pm_attendenceList, name='pm_attendenceList'),
    path('pm_TL_attendence', views.pm_TL_attendence, name='pm_TL_attendence'),
    path('pm_TL_attendencelist', views.pm_TL_attendencelist, name='pm_TL_attendencelist'),
    path('pm_developer_attendence', views.pm_developer_attendence, name='pm_developer_attendence'),
    path('pm_developer_attendencelist', views.pm_developer_attendencelist, name='pm_developer_attendencelist'),
    
]

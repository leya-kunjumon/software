from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [

    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('software/', views.software, name='software'),

    # ***********************developer***********************************************

    path('developer_Dashboard/', views.developer_Dashboard,name='developer_Dashboard'),
    path('developer_task/', views.developer_task, name='developer_task'),
    path('developer_task_form/', views.developer_task_form,name='developer_task_form'),
    path('developer_project_table/', views.developer_project_table,name='developer_project_table'),
    path('developer_attendance/', views.developer_attendance,name='developer_attendance'),
    path('developer_attendance_list/', views.developer_attendance_list,name='developer_attendance_list'),
    path('developer_reportedissue/', views.developer_reportedissue,name='developer_reportedissue'),
    path('developer_reportedissues/', views.developer_reportedissues,name='developer_reportedissues'),
    path('developer_reportissue/', views.developer_reportissue,name='developer_reportissue'),
    path('developer_applyleave/', views.developer_applyleave,name='developer_applyleave'),
    path('developer_apply_leave/', views.developer_apply_leave,name='developer_apply_leave'),
    path('developer_apply_leave_list/', views.developer_apply_leave_list,name='developer_apply_leave_list'),
    path('developer_account_settings/', views.developer_account_settings,name='developer_account_settings'),
    path('developer_change_password/', views.developer_change_password,name='developer_change_password'),

    # **************************** TESTER ********************************

    path('tester_dashboard/', views.tester_dashboard, name='tester_dashboard'),
    path('tester_task/', views.tester_task, name='tester_task'),
    path('tester_taskassigned/', views.tester_taskassigned,name='tester_taskassigned'),
    path('tester_taskpending/', views.tester_taskpending,name='tester_taskpending'),
    path('tester_projects/', views.tester_projects, name='tester_projects'),
    path('tester_projectdetails/', views.tester_projectdetails,name='tester_projectdetails'),

    # ***************************** Project Manager ******************************

    path('pm_Dashboard/', views.pm_Dashboard, name='pm_Dashboard'),
    path('pm_projects/', views.pm_projects, name='pm_projects'),
    path('pm_upcomingProject/', views.pm_upcomingProject,name='pm_upcomingProject'),
    path('pm_currentProject/', views.pm_currentProject, name='pm_currentProject'),
    path('pm_completedProject/', views.pm_completedProject,name='pm_completedProject'),
    path('pm_createProject/', views.pm_createProject, name='pm_createProject'),
    path('pm_newProj_status/', views.pm_newProj_status, name='pm_newProj_status'),
    path('pm_assignProject/', views.pm_assignProject, name='pm_assignProject'),
    path('pm_newProject/', views.pm_newProject, name='pm_newProject'),
    path('pm_acceptedProject/', views.pm_acceptedProject,name='pm_acceptedProject'),
    path('pm_rejectedProject/', views.pm_rejectedProject,name='pm_rejectedProject'),
    path('pm_currentProjectFirst/', views.pm_currentProjectFirst,name='pm_currentProjectFirst'),
    path('pm_currentprojectTeam/', views.pm_currentprojectTeam,name='pm_currentprojectTeam'),
    path('pm_currentprojectTeamList/', views.pm_currentprojectTeamList,name='pm_currentprojectTeamList'),
    path('pm_completedFirst/', views.pm_completedFirst, name='pm_completedFirst'),
    path('pm_completeProj_Team/', views.pm_completeProj_Team,name='pm_completeProj_Team'),
    path('pm_completeProj_Teamlist/', views.pm_completeProj_Teamlist,name='pm_completeProj_Teamlist'),
    path('pm_employee/', views.pm_employee, name='pm_employee'),
    path('pm_employee_TL/', views.pm_employee_TL, name='pm_employee_TL'),
    path('pm_employee_developer/', views.pm_employee_developer,name='pm_employee_developer'),
    path('pm_emp_developers_dashboard/', views.pm_emp_developers_dashboard,name='pm_emp_developers_dashboard'),
    path('pm_developer_team/', views.pm_developer_team, name='pm_developer_team'),
    path('pm_TL_Team/', views.pm_TL_Team, name='pm_TL_Team'),
    path('pm_TL_Team_profile/', views.pm_TL_Team_profile,name='pm_TL_Team_profile'),
    path('pm_TL_Team_involved/', views.pm_TL_Team_involved,name='pm_TL_Team_involved'),
    path('pm_TL_Team_attendence/', views.pm_TL_Team_attendence,name='pm_TL_Team_attendence'),
    path('pm_TL_Team_viewAttendence/', views.pm_TL_Team_viewAttendence,name='pm_TL_Team_viewAttendence'),
    path('pm_tl_dashboard/', views.pm_tl_dashboard, name='pm_tl_dashboard'),
    path('pm_reportedIssues/', views.pm_reportedIssues, name='pm_reportedIssues'),
    path('pm_report_reportedIssue/', views.pm_report_reportedIssue,name='pm_report_reportedIssue'),
    path('pm_reportedIssue_action/', views.pm_reportedIssue_action,name='pm_reportedIssue_action'),
    path('pm_report_issue/', views.pm_report_issue, name='pm_report_issue'),
    path('pm_tl_reported_issues/', views.pm_tl_reported_issues,name='pm_tl_reported_issues'),
    path('pm_tl_issuesVerified/', views.pm_tl_issuesVerified,name='pm_tl_issuesVerified'),
    path('pm_applyLeave/', views.pm_applyLeave, name='pm_applyLeave'),
    path('pm_applyleave_Form/', views.pm_applyleave_Form,name='pm_applyleave_Form'),
    path('pm_requested_leave/', views.pm_requested_leave,name='pm_requested_leave'),
    path('pm_Attendence/', views.pm_Attendence, name='pm_Attendence'),
    path('pm_attendenceList/', views.pm_attendenceList, name='pm_attendenceList'),
    path('pm_TL_attendence/', views.pm_TL_attendence, name='pm_TL_attendence'),
    path('pm_TL_attendencelist/', views.pm_TL_attendencelist,name='pm_TL_attendencelist'),
    path('pm_developer_attendence/', views.pm_developer_attendence,name='pm_developer_attendence'),
    path('pm_developer_attendencelist/', views.pm_developer_attendencelist,name='pm_developer_attendencelist'),

    # ********************************* Manager *****************************************

    path('manager_Dashboard/', views.manager_Dashboard, name='manager_Dashboard'),
    path('manager_dept/', views.manager_dept, name='manager_dept'),
    path('manager_emp_dept/', views.manager_emp_dept, name='manager_emp_dept'),
    path('manager_projects/', views.manager_projects, name='manager_projects'),
    path('manager_proj_list/', views.manager_proj_list, name='manager_proj_list'),
    path('manager_proj_details/', views.manager_proj_details,name='manager_proj_details'),
    path('manager_proj_manager/', views.manager_proj_manager,name='manager_proj_manager'),
    path('manager_proj_manager1/', views.manager_proj_manager1,name='manager_proj_manager1'),
    path('manager_proj_manager2/', views.manager_proj_manager2,name='manager_proj_manager2'),
    path('manager_completed_proj/', views.manager_completed_proj,name='manager_completed_proj'),
    path('manager_completed_proj_details/', views.manager_completed_proj_details,name='manager_completed_proj_details'),
    path('manager_completed_proj_manager/', views.manager_completed_proj_manager,name='manager_completed_proj_manager'),
    path('manager_completed_proj_manager_list/', views.manager_completed_proj_manager_list,name='manager_completed_proj_manager_list'),
    path('manager_completed_proj_manager_tl/', views.manager_completed_proj_manager_tl,name='manager_completed_proj_manager_tl'),
    path('manager_emp_dept_list/', views.manager_emp_dept_list,name='manager_emp_dept_list'),
    path('manager_emp_dept_details/', views.manager_emp_dept_details,name='manager_emp_dept_details'),
    path('manager_emp_profile/', views.manager_emp_profile,name='manager_emp_profile'),
    path('manager_emp_involved_projects/', views.manager_emp_involved_projects,name='manager_emp_involved_projects'),
    path('manager_emp_attendance/', views.manager_emp_attendance,name='manager_emp_attendance'),
    path('manager_emp_attendance_show/', views.manager_emp_attendance_show,name='manager_emp_attendance_show'),
    path('manager_upcoming/', views.manager_upcoming, name='manager_upcoming'),
    path('manager_createproject/', views.manager_createproject,name='manager_createproject'),
    path('manager_upcoming_project/', views.manager_upcoming_project,name='manager_upcoming_project'),
    path('manager_give_project/', views.manager_give_project,name='manager_give_project'),
    path('manager_accepted_project/', views.manager_accepted_project,name='manager_accepted_project'),
    path('manager_rejected_project/', views.manager_rejected_project,name='manager_rejected_project'),
    path('manager_task/', views.manager_task, name='manager_task'),
    path('manager_givetask/', views.manager_givetask, name='manager_givetask'),
    path('manager_current_task/', views.manager_current_task,name='manager_current_task'),
    path('manager_previous_task/', views.manager_previous_task,name='manager_previous_task'),
    path('manager_registration_details/', views.manager_registration_details,name='manager_registration_details'),
    path('manager_new_department/', views.manager_new_department,name='manager_new_department'),
    path('manager_create_department/', views.manager_create_department,name='manager_create_department'),
    path('manager_attendance/', views.manager_attendance,name='manager_attendance'),
    path('manager_attendance_show/', views.manager_attendance_show,name='manager_attendance_show'),
    path('manager_reported_issues/', views.manager_reported_issues,name='manager_reported_issues'),
    path('manager_issues/', views.manager_issues, name='manager_issues'),
    path('manager_issues_form/', views.manager_issues_form,name='manager_issues_form'),
    path('manager_myissues/', views.manager_myissues, name='manager_myissues'),
    path('manager_reported_detail/', views.manager_reported_detail,name='manager_reported_detail'),
    path('manager_reported_issue_show/', views.manager_reported_issue_show,name='manager_reported_issue_show'),

    # ***************************** Admin ******************************

    path('admin_Dashboard/', views.admin_Dashboard, name='admin_Dashboard'),
    path('admin_dept/', views.admin_dept, name='admin_dept'),
    path('admin_emp_dept/', views.admin_emp_dept, name='admin_emp_dept'),
    path('admin_projects/', views.admin_projects, name='admin_projects'),
    path('admin_proj_list/', views.admin_proj_list, name='admin_proj_list'),
    path('admin_proj_details/', views.admin_proj_details,name='admin_proj_details'),
    path('admin_proj_manager/', views.admin_proj_manager,name='admin_proj_manager'),
    path('admin_proj_manager1/', views.admin_proj_manager1,name='admin_proj_manager1'),
    path('admin_proj_manager2/', views.admin_proj_manager2,name='admin_proj_manager2'),
    path('admin_completed_proj/', views.admin_completed_proj,name='admin_completed_proj'),
    path('admin_completed_proj_details/', views.admin_completed_proj_details,name='admin_completed_proj_details'),
    path('admin_completed_proj_manager/', views.admin_completed_proj_manager,name='admin_completed_proj_manager'),
    path('admin_completed_proj_manager_list/', views.admin_completed_proj_manager_list,name='admin_completed_proj_manager_list'),
    path('admin_completed_proj_manager_tl/', views.admin_completed_proj_manager_tl,name='admin_completed_proj_manager_tl'),
    path('admin_emp_dept_list/', views.admin_emp_dept_list,name='admin_emp_dept_list'),
    path('admin_emp_dept_details/', views.admin_emp_dept_details,name='admin_emp_dept_details'),
    path('admin_emp_profile/', views.admin_emp_profile, name='admin_emp_profile'),
    path('admin_emp_involved_projects/', views.admin_emp_involved_projects,name='admin_emp_involved_projects'),
    path('admin_emp_attendance/', views.admin_emp_attendance,name='admin_emp_attendance'),
    path('admin_emp_attendance_show/', views.admin_emp_attendance_show,name='admin_emp_attendance_show'),
    path('admin_upcoming/', views.admin_upcoming, name='admin_upcoming'),
    path('admin_createproject/', views.admin_createproject,name='admin_createproject'),
    path('admin_upcoming_project/', views.admin_upcoming_project,name='admin_upcoming_project'),
    path('admin_give_project/', views.admin_give_project,name='admin_give_project'),
    path('admin_accepted_project/', views.admin_accepted_project,name='admin_accepted_project'),
    path('admin_rejected_project/', views.admin_rejected_project,name='admin_rejected_project'),
    path('admin_task/', views.admin_task, name='admin_task'),
    path('admin_givetask/', views.admin_givetask, name='admin_givetask'),
    path('admin_current_task/', views.admin_current_task,name='admin_current_task'),
    path('admin_previous_task/', views.admin_previous_task,name='admin_previous_task'),
    path('admin_registration_details/', views.admin_registration_details,name='admin_registration_details'),
    path('admin_new_department/', views.admin_new_department,name='admin_new_department'),
    path('admin_create_department/', views.admin_create_department,name='admin_create_department'),
    path('admin_attendance/', views.admin_attendance, name='admin_attendance'),
    path('admin_attendance_show/', views.admin_attendance_show,name='admin_attendance_show'),
    path('admin_reported_issues/', views.admin_reported_issues,name='admin_reported_issues'),
    path('admin_emp_reported_detail/', views.admin_emp_reported_detail,name='admin_emp_reported_detail'),
    path('admin_emp_reported_issue_show/', views.admin_emp_reported_issue_show,name='admin_emp_reported_issue_show'),
    path('admin_manager_reported_detail/', views.admin_manager_reported_detail,name='admin_manager_reported_detail'),
    path('admin_manager_reported_issue_show/', views.admin_manager_reported_issue_show,name='admin_manager_reported_issue_show'),

    # *******************************TL********************************************

    path('index_tl/', views.index_tl, name='index_tl'),
    path('tlproject/', views.tlproject, name='tlproject'),
    path('tlproject_task/', views.tlproject_task, name='tlproject_task'),
    path('tl_project_splittask/', views.tl_project_splittask,name='tl_project_splittask'),
    path('tl_projecttask_status/', views.tl_projecttask_status,name='tl_projecttask_status'),
    path('tl_addtask/', views.tl_addtask, name='tl_addtask'),
    path('attendance_tl/', views.attendance_tl, name='attendance_tl'),
    path('tl_attendance_sort/', views.tl_attendance_sort,name='tl_attendance_sort'),
    path('tl_reportissue/', views.tl_reportissue, name='tl_reportissue'),
    path('tl_reportissue_table/', views.tl_reportissue_table,name='tl_reportissue_table'),
    path('tl_reportissue_submit/', views.tl_reportissue_submit,name='tl_reportissue_submit'),
    path('tl_reportissue_register/', views.tl_reportissue_register,name='tl_reportissue_register'),
    path('tl_reportissue_success/', views.tl_reportissue_success,name='tl_reportissue_success'),
    path('tl_developreport/', views.tl_developreport, name='tl_developreport'),
    path('tl_developer_view/', views.tl_developer_view, name='tl_developer_view'),
    path('tl_task/', views.tl_task, name='tl_task'),
    path('tl_taskpending/', views.tl_taskpending, name='tl_taskpending'),
    path('tl_tasksubmit/', views.tl_tasksubmit, name='tl_tasksubmit'),
    path('tl_leave/', views.tl_leave, name='tl_leave'),
    path('tl_leaverequest/', views.tl_leaverequest, name='tl_leaverequest'),
    path('tl_leaverequest_view/', views.tl_leaverequest_view,name='tl_leaverequest_view'),

    # **************************project**************************

    path('project_details/', views.project_details, name='project_details'),

    # ************************** client  **************************

    path('client_card/', views.client_card, name='client_card'),
    path('client_details/', views.client_details, name='client_details'),

    # *************************  hr  ****************************
    path('base_hr/', views.base_hr, name='base_hr'),
    path('hr_Dashboard/', views.hr_Dashboard, name='hr_Dashboard'),
    path('hr_view_attendance/', views.hr_view_attendance,name='hr_view_attendance'),
    path('hr_view_attendance_list/', views.hr_view_attendance_list,name='hr_view_attendance_list'),
    path('hr_vacancy_list/', views.hr_vacancy_list, name='hr_vacancy_list'),
    path('hr_vacancy_details/', views.hr_vacancy_details,name='hr_vacancy_details'),

    # **************************** Digital Marketing ****************

    path('digitalmarketing_card/', views.digitalmarketing_card,name="digitalmarketing_card"),
    path('marketingtl_Dashboard', views.marketingtl_Dashboard,name="marketingtl_Dashboard"),
    path('datacollector_Dashboard', views.datacollector_Dashboard,name="datacollector_Dashboard"),
    path('marketingexecutive_Dashboard', views.marketingexecutive_Dashboard,name="marketingexecutive_Dashboard"),
    path('datacollector_attendance', views.datacollector_attendance,name="datacollector_attendance"),
    path('datacollector_attendance_list/', views.datacollector_attendance_list,name="datacollector_attendance_list"),
    path('datacollector_reportedissue/', views.datacollector_reportedissue,name="datacollector_reportedissue"),
    path('datacollector_reportissue_form/', views.datacollector_reportissue_form,name="datacollector_reportissue_form"),
    path('datacollector_reportedissue_table/', views.datacollector_reportedissue_table,name="datacollector_reportedissue_table"),
    path('marketingexecutive_attendance/', views.marketingexecutive_attendance,name="marketingexecutive_attendance"),
    path('marketingexecutive_attendance_list/', views.marketingexecutive_attendance_list,name="dmarketingexecutive_attendance_list"),
    path('marketingexecutive_reportedissue/', views.marketingexecutive_reportedissue,name="marketingexecutive_reportedissue"),
    path('marketingexecutive_reportissue_form/', views.marketingexecutive_reportissue_form,name="marketingexecutive_reportissue_form"),
    path('marketingexecutive_reportedissue_table/', views.marketingexecutive_reportedissue_table,name="marketingexecutive_reportedissue_table"),
    path('marketingtl_reportedissue/', views.marketingtl_reportedissue,name="marketingtl_reportedissue"),
    path('marketingtl_reportissue_form/', views.marketingtl_reportissue_form,name="marketingtl_reportissue_form"),
    path('marketingtl_reportedissue_table/', views.marketingtl_reportedissue_table,name="marketingtl_reportedissue_table"),
    path('marketingtl_attendance/', views.marketingtl_attendance,name="marketingtl_attendance"),
    path('marketingtl_attendance_datacollector/', views.marketingtl_attendance_datacollector,name="marketingtl_attendance_datacollector"),
    path('marketingtl_attendance_executive/', views.marketingtl_attendance_executive,name="marketingtl_attendance_executive"),
    path('marketingtl_attendance_datacollectorview/', views.marketingtl_attendance_datacollectorview,name="marketingtl_attendance_datacollectorview"),
    path('marketingtl_attendance_executiveview/', views.marketingtl_attendance_executiveview,name="marketingtl_attendance_executiveview"),
    path('marketingtl_attendance_datacollectorview_list/', views.marketingtl_attendance_datacollectorview_list,name="marketingtl_attendance_datacollectorview_list"),
    path('marketingtl_attendance_executiveview_list/', views.marketingtl_attendance_executiveview_list,name="marketingtl_attendance_executiveview_list"),
    path('marketingtl_attendance_datacollectoradd/', views.marketingtl_attendance_datacollectoradd,name="marketingtl_attendance_datacollectoradd"),
    path('marketingtl_attendance_executiveadd/', views.marketingtl_attendance_executiveadd,name="marketingtl_attendance_executiveadd"),
    path('marketingtl_attendance_view/', views.marketingtl_attendance_view,
         name="marketingtl_attendance_view"),

    path('marketingtl_attendance_view_list/', views.marketingtl_attendance_view_list,
         name="marketingtl_attendance_view_list"),

    path('marketingtl_mytask/', views.marketingtl_mytask,
         name="marketingtl_mytask"),

    path('marketingexecutive_mytask/', views.marketingexecutive_mytask,
         name="marketingexecutive_mytask"),

    path('marketingtl_sharedtask/', views.marketingtl_sharedtask,
         name="marketingtl_sharedtask"),

    path('datacollector_mytask/', views.datacollector_mytask,
         name="datacollector_mytask"),


    path('marketingtl_products_table/', views.marketingtl_products_table,
         name="marketingtl_products_table"),

    path('marketingtl_recruitments_table/', views.marketingtl_recruitments_table,
         name="marketingtl_recruitments_table"),

    path('marketingtl_products_details/', views.marketingtl_products_details,
         name="marketingtl_products_details"),

    path('marketingtl_recruitments_details/', views.marketingtl_recruitments_details,
         name="marketingtl_recruitments_details"),


    path('datacollector_products_table/', views.datacollector_products_table,
         name="datacollector_products_table"),

    path('datacollector_recruitments_table/', views.datacollector_recruitments_table,
         name="datacollector_recruitments_table"),

    path('datacollector_products_details/', views.datacollector_products_details,
         name="datacollector_products_details"),

    path('datacollector_recruitments_details/', views.datacollector_recruitments_details,
         name="datacollector_recruitments_details"),


    path('marketingexecutive_products_table/', views.marketingexecutive_products_table,
         name="marketingexecutive_products_table"),

    path('marketingexecutive_recruitments_table/', views.marketingexecutive_recruitments_table,
         name="marketingexecutive_recruitments_table"),

    path('marketingexecutive_products_details/', views.marketingexecutive_products_details,
         name="marketingexecutive_products_details"),

    path('marketingexecutive_recruitments_details/', views.marketingexecutive_recruitments_details,
         name="marketingexecutive_recruitments_details"),


    path('marketingexecutive_products_data/', views.marketingexecutive_products_data,
         name="marketingexecutive_products_data"),

    path('marketingexecutive_recruitments_data/', views.marketingexecutive_recruitments_data,
         name="marketingexecutive_recruitments_data"),


    path('datacollector_products_collectdata/', views.datacollector_products_collectdata,
         name="datacollector_products_collectdata"),

    path('datacollector_recruitments_collectdata/', views.datacollector_recruitments_collectdata,
         name="datacollector_recruitments_collectdata"),


    path('marketingtl_shtask_products_table/', views.marketingtl_shtask_products_table,
         name="marketingtl_shtask_products_table"),

    path('marketingtl_shtask_recruitments_table/', views.marketingtl_shtask_recruitments_table,
         name="marketingtl_shtask_recruitments_table"),

    path('marketingtl_shtask_products_details/', views.marketingtl_shtask_products_details,
         name="marketingtl_shtask_products_details"),

    path('marketingtl_shtask_recruitments_details/', views.marketingtl_shtask_recruitments_details,
         name="marketingtl_shtask_recruitments_details"),


    path('marketingtl_products_data/', views.marketingtl_products_data,
         name="marketingtl_products_data"),

    path('marketingtl_recruitments_data/', views.marketingtl_recruitments_data,
         name="marketingtl_recruitments_data"),
 
 #**********************Training project ******************
 #***********************course***********************************************
    path('training/',views.trainings, name='training'),
    path('course/',views.course, name='course'),
    path('course_add/',views.course_add, name='course_add'),
    path('course_addnew/',views.course_addnew, name='course_addnew'),
    path('course_category/',views.course_category, name='course_category'),
    path('course_courses/',views.course_courses, name='course_courses'),
    path('course_course_details/',views.course_course_details, name='course_course_details'),

]

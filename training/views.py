from django.shortcuts import render
# Create your views here. 
def index(request):
    return render(request,'training\index.html')
    
def Trainings(request):
    return render(request,'training\Training.html')

#***********************course**************************************************

def course(request):
    return render(request,'training\course\course.html')

def course_add(request):
    return render(request,'training\course\course_add.html')

def course_addnew(request):
    return render(request,'training\course\course_addnew.html')

def course_category(request):
    return render(request,'training\course\course_category.html')

def course_courses(request):
    return render(request,'training\course\course_courses.html')
    
def course_course_details(request):
    return render(request,'training\course\course_course_details.html')

#******************Manager*****************************

def manager_Dashboard(request):
    return render(request,'training\manager\manager_Dashboard.html')

def manager_categories(request):
    return render(request,'training\manager\manager_categories.html') 

def manager_emp_categories(request):
    return render(request,'training\manager\manager_emp_categories.html')   

def manager_course(request):
    return render(request,'training\manager\manager_course.html')

def manager_emp_course_list(request):
    return render(request,'training\manager\manager_emp_course_list.html')

def manager_emp_course_details(request):
    return render(request,'training\manager\manager_emp_course_details.html')

def manager_emp_profile(request):
    return render(request,'training\manager\manager_emp_profile.html')

def manager_emp_involved_projects(request):
    return render(request,'training\manager\manager_emp_involved_projects.html')
    
def manager_emp_attendance(request):
    return render(request,'training\manager\manager_emp_attendance.html')

def manager_emp_attendance_show(request):
    return render(request,'training\manager\manager_emp_attendance_show.html')

def manager_task(request):
    return render(request,'training\manager\manager_task.html')

def manager_givetask(request):
    return render(request,'training\manager\manager_givetask.html')

def manager_current_task(request):
    return render(request,'training\manager\manager_current_task.html')

def manager_previous_task(request):
    return render(request,'training\manager\manager_previous_task.html')

def manager_registration_details(request):
    return render(request,'training\manager\manager_registration_details.html')  

def manager_attendance(request):
    return render(request,'training\manager\manager_attendance.html') 

def manager_attendance_show(request):
    return render(request,'training\manager\manager_attendance_show.html')

def manager_reported_issues(request):
    return render(request,'training\manager\manager_reported_issues.html') 

def manager_issues(request):
    return render(request,'training\manager\manager_issues.html')

def manager_issues_form(request):
    return render(request,'training\manager\manager_issues_form.html')

def manager_myissues(request):
    return render(request,'training\manager\manager_myissues.html')

def manager_reported_detail(request):
    return render(request,'training\manager\manager_reported_detail.html')

def manager_reported_issue_show(request):
    return render(request,'training\manager\manager_reported_issue_show.html')

#******************Trainer*****************************

def trainer_dashboard(request):
    return render(request,'training/trainer/trainer_dashboard.html')

def trainer_applyleave(request):
    return render(request, 'training/trainer/trainer_applyleave.html')

def trainer_applyleave_form(request):
    return render(request, 'training/trainer/trainer_applyleave_form.html')

def trainer_traineesleave_table(request):
    return render(request, 'training/trainer/trainer_traineesleave_table.html')

def trainer_reportissue(request):
    return render(request, 'training/trainer/trainer_reportissue.html')

def trainer_reportissue_form(request):
    return render(request, 'training/trainer/trainer_reportissue_form.html')

def trainer_reportedissue_table(request):
    return render(request, 'training/trainer/trainer_reportedissue_table.html')

def trainer_topic(request):
    return render(request,'training/trainer/trainer_topic.html')

def trainer_addtopic(request):
    return render(request,'training/trainer/trainer_addtopic.html')

def trainer_viewtopic(request):
    return render(request,'training/trainer/trainer_viewtopic.html')

def trainer_attendance(request):
    return render(request,'training/trainer/trainer_attendance.html')

def trainer_attendance_trainees(request):
    return render(request,'training/trainer/trainer_attendance_trainees.html')

def trainer_attendance_trainer(request):
    return render(request, 'training/trainer/trainer_attendance_trainer.html')

def trainer_attendance_trainer_viewattendance(request):
    return render(request,'training/trainer/trainer_attendance_trainer_viewattendance.html')

def trainer_attendance_trainer_viewattendancelist(request):
    return render(request,'training/trainer/trainer_attendance_trainer_viewattendancelist.html')

def trainer_team(request):
    return render(request,'training/trainer/trainer_team.html')

def trainer_currentteam(request):
    return render(request,'training/trainer/trainer_current_team_list.html')

def trainer_currenttrainees(request):
    return render(request, 'training/trainer/trainer_current_trainees_list.html')

def trainer_currenttraineesdetails(request):
    return render(request,'training/trainer/trainer_current_tainees_details.html')

def trainer_currentattentable(request):
    return render(request,'training/trainer/trainer_current_atten_table.html')

def trainer_currentperform(request):
    return render(request,'training/trainer/trainer_current_perform.html')

def trainer_currentattenadd(request):
    return render(request,'training/trainer/trainer_current_atten_add.html')

def trainer_previousteam(request):
    return render(request,'training/trainer/trainer_previous_team_list.html')

def trainer_previoustrainees(request):
    return render(request,'training/trainer/trainer_previous_trainess_list.html')

def trainer_previoustraineesdetails(request):
    return render(request, 'training/trainer/trainer_previous_trainees_details.html')

def trainer_previousattentable(request):
    return render(request,'training/trainer/trainer_previous_atten_table.html')

def trainer_previousperfomtable(request):
    return render(request,'training/trainer/trainer_previous_performtable.html')

def trainer_current_attendance(request):
    return render(request,'training/trainer/trainer_current_attendance.html')

def trainer_Task(request) :
    return render(request,'training/trainer/trainer_task.html')
    
def trainer_teamlistpage(request) :
    return render(request,'training/trainer/trainer_teamlist.html')
    
def trainer_taskpage(request) :
    return render(request, 'training/trainer/trainer_taskfor.html')
    
def trainer_givetask(request) :
    return render(request, 'training/training/trainer/trainer_givetask.html')
    
def trainer_taskgivenpage(request) :
    return render(request,'training/trainer/trainer_taskgiven.html')
    
def trainer_taska(request):
    return render(request, 'training/trainer/trainer_taska.html')

def trainer_task_completed_teamlist(request):
    return render(request, 'training/trainer/trainer_task_completed_teamlist.html')

def trainer_task_completed_team_tasklist(request):
    return render(request, 'training/trainer/trainer_task_completed_team_tasklist.html')

def trainer_task_previous_teamlist(request):
    return render(request, 'training/trainer/trainer_task_previous_teamlist.html')

def trainer_task_previous_team_tasklist(request):
    return render(request, 'training/trainer/trainer_task_previous_team_tasklist.html')

def trainer_trainees(request):
    return render(request, 'training/trainer/trainer_trainees.html')

def trainer_previous_trainees(request):
    return render(request,'training/trainer/trainer_previous_trainees.html')

def trainer_current_trainees(request):
    return render(request,'training/trainer/trainer_current_trainees.html')

def trainer_myreportissue_table(request):
    return render(request, 'training/trainer/trainer_myreportissue_table.html')

def trainer_current_attendance_view(request):
    return render(request,'training/trainer/trainer_current_attendance_view.html')

def trainer_attendance_trainees_viewattendance(request):
    return render(request,'training/trainer/trainer_attendance_trainees_viewattendance.html')

def trainer_attendance_trainees_viewattendancelist(request):
    return render(request,'training/trainer/trainer_attendance_trainees_viewattendancelist.html')

def trainer_attendance_trainees_addattendance(request):
    return render(request,'training/trainer/trainer_attendance_trainees_addattendance.html')
    
#******************  Trainee  *****************************

def trainee_dashboard_trainee(request):
    return render(request,'training/trainee/trainee_dashboard_trainee.html')
    
def trainee_task(request):
   return render(request,'training/trainee/trainee_task.html')   

def trainee_task_list(request):
    return render(request,'training/trainee/trainee_task_list.html')

def trainee_task_details(request):
    return render(request,'training/trainee/trainee_task_details.html')

def trainee_completed_taskList(request):
   return render(request,'training/trainee/trainee_completed_taskList.html')

def trainee_completedTask(request):
    return render(request,'training/trainee/trainee_completedTask.html')

def trainee_completed_details(request):
    return render(request,'training/trainee/trainee_completed_details.html')

def trainee_topic(request):
    return render(request, 'training/trainee/trainee_topic.html')

def trainee_currentTopic(request):
    return render(request, 'training/trainee/trainee_currentTopic.html')
    
def trainee_previousTopic(request):
    return render(request, 'training/trainee/trainee_previousTopic.html')

def trainee_reported_issue(request):
    return render(request, 'training/trainee/trainee_reported_issue.html')
   
def trainee_report_reported(request):
    return render(request, 'training/trainee/trainee_report_reported.html')
  
def trainee_report_issue(request):
    return render(request, 'training/trainee/trainee_report_issue.html')

def trainee_applyleave_form(request):
    return render(request, 'training/trainee/trainee_applyleave_form.html')  

def trainee_applyleave_card(request):
     return render(request, 'training/trainee/trainee_applyleave_cards.html')
    
def trainee_appliedleave(request):
     return render(request, 'training/trainee/trainee_appliedleave.html')
    
def Attendance(request):
   return render(request,'training/trainee/trainees_attendance.html')
    
def trainees_attendance_viewattendance(request):
    return render(request,'training/trainee/trainees_attendance_viewattendance.html')
 
def trainees_attendance_viewattendancelist(request):
   return render(request,'training/trainee/trainees_attendance_viewattendancelist.html')
   
def trainee_payment(request):
   return render(request,'training/trainee/trainee_payment.html')
   
def trainee_payment_addpayment(request):
   return render(request,'training/trainee/trainee_payment_addpayment.html')
  
def trainee_payment_viewpayment(request):
     return render(request,'training/trainee/trainee_payment_viewpayment.html')
                
  

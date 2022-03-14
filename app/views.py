from django.shortcuts import render

# Create your views here.


#***********************developer**************************************************
def developer_Dashboard(request):
    return render(request,'developer\developer_Dashboard.html')

def developer_task(request):
    return render(request,'developer\developer_task.html')

def developer_task_form(request):
    return render(request,'developer\developer_task_form.html')
def developer_project(request):
    return render(request,'developer\developer_project.html')
def developer_project_table(request):
    return render(request,'developer\developer_project_table.html')
def developer_attendance(request):
    return render(request,'developer\developer_attendance.html')
def developer_attendance_list(request):
    return render(request,'developer\developer_attendance_list.html')
def developer_reportedissue(request):
    return render(request,'developer\developer_reportedissue.html')
def developer_reportedissues(request):
    return render(request,'developer\developer_reportedissues.html')
def developer_reportissue(request):
    return render(request,'developer\developer_reportissue.html')

def developer_applyleave(request):
    return render(request,'developer\developer_applyleave.html')
def developer_apply_leave(request):
    return render(request,'developer\developer_apply_leave.html')    
def developer_apply_leave_list(request):
    return render(request,'developer\developer_apply_leave_list.html')

def developer_account_settings(request):
    return render(request,'developer\developer_account_settings.html')
def developer_change_password(request):
    return render(request,'developer\developer_change_password.html')





#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')


#****************** Project Manager ******************************************
    

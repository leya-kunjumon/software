from django.shortcuts import render

# Create your views here.


#***********************developer***********************************************
def index(request):
    return render(request,'index.html')



#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')

######################### TESTER #################################

def tester_dashboard(request):
    return render(request,'tester/tester_dashboard.html')  
    

def tester_task(request):
    return render(request, 'tester/tester_task.html')


def tester_taskassigned(request):
    return render(request, 'tester/tester_taskassigned.html')


def tester_taskpending(request):
    return render(request, 'tester/tester_taskpending.html')
    

def tester_projects(request):
    return render(request, 'tester/tester_projects.html')
    

def tester_projectdetails(request):
    return render(request, 'tester/tester_projectdetails.html')

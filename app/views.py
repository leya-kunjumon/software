from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request,'index.html')

def software(request):
    return render(request,'software.html')
    
#***********************developer***********************************************




#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')


#****************** Project Manager ******************************************
    

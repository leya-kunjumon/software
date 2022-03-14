from django.shortcuts import render

# Create your views here.


#***********************developer***********************************************
def developer_Dashboard(request):
    return render(request,'developer\developer_Dashboard.html')



#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')


#****************** Project Manager ******************************************
    

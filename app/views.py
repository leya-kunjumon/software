from django.shortcuts import render

# Create your views here.


#***********************developer***********************************************
def index(request):
    return render(request,'index.html')



#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')


#****************** Project Manager ******************************************
    

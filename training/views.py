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
from django.shortcuts import render
from courses.models import Course
# Create your views here.

def home(request):
    home_courses = Course.objects.all()
    return render(request, 'home.html',{'homecourses':home_courses})

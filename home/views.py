from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    studentVar = Student.objects.all()
    return render(request, 'index.html', {'students': studentVar})
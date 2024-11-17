from django.shortcuts import render, redirect
from . import models

# Create your views here.
def home(request):
   students = models.Student.objects.all()
   return render(request, 'tech/home.html', {'students': students})
def student(request):
   if request.method == 'POST':
      fname = request.POST['fname']
      lname = request.POST['lname']
      email = request.POST['email']
      age = request.POST['age']
      phone = request.POST['phone']
      profile = request.FILES['profile']
      
      # Save the data to the database
      # (Assuming 'Student' is a model in your database)
      student = models.Student(fname=fname, lname=lname, email=email, age=age, phone=phone, profile=profile)
      student.save()
      return redirect('home')
      
   return render(request, 'tech/student.html')
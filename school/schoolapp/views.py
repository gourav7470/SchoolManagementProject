from django.shortcuts import HttpResponse, redirect, render
from schoolapp.models import  Student

def home(request):
 return render(request,"index.html")

def new_student_form(request):
  if request.method == "POST":
   req=request.POST
   first_name = req.get('first_name')
   last_name = req.get('last_name')
   gender = req.get('gender')
   father_name = req.get('father_name')
   mother_name = req.get('mother_name')
   dob = req.get('dob')
   class_class = req.get('class_class')
   mobile = req.get('mobile')
   address = req.get('address')
   email = req.get('email')
   aadhar = req.get('aadhar_card')
   
   stu = Student.objects.create(
    first_name = first_name,
    last_name = last_name,
    father_name = father_name,
    mother_name = mother_name,
    dob = dob,
    gender = gender,
    aadhar = aadhar,
    class_class = class_class,
    mobile = mobile,
    email = email,
    address = address,
   )
   stu.save()
   return redirect('stddateils')
  context ={
   'CLASS_CHOICES': Student.CLASS_CHOICES,
  }
  return render(request,"newStudentForm.html", context)

def stddateils(request):
 stu = Student.objects.all()
 context = {
  'stu':stu,
 }
 return render(request,'stddateils.html',context)

def update_form(request,id):
 stu = Student.objects.get(id=id)
 if request.method == "POST":
   req=request.POST
   formfields = {
    'first_name' : req.get('first_name'),
    'last_name' : req.get('last_name'),
    'father_name' : req.get('father_name'),
    'mother_name' : req.get('mother_name'),
    'dob' : req.get('dob'),
    'class_class' : req.get('class_class'),
    'mobile' : req.get('mobile'),
    'address' : req.get('address'),
    'dob' : req.get('dob'),
    'email': req.get('email'),
    'aadhar': req.get('aadhar'),
   }
   for key, value in formfields.items():
    if value:
     setattr(stu, key, value)
   stu.save()
   return redirect('stddateils')
 context = {
  'stu':stu,
  'CLASS_CHOICES': Student.CLASS_CHOICES,
 }
 return render(request,"update.html",context)

def dalete_form(request,id):
 stu = Student.objects.get(id=id)
 stu.delete()

 return redirect('stddateils')

def login(request):
 return render(request,"login.html")




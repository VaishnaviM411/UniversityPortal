
from email.utils import decode_params
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from numpy import object_

from .models import *

class Login(View):
    def get(self, request, template_name='login.html'):
        return render(request,template_name)

    def post(self,request,template_name='login.html'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request,'Logged in successfully.')
                message = {}
                
                print(user.groups.all())
                if user.groups.filter(name='portal_admin').exists():
                    return redirect('AdminDashboard')
                elif user.groups.filter(name='instructor').exists():
                    return redirect('InstructorDashboard')
                elif user.groups.filter(name='student').exists():
                    return redirect('StudentDashboard')
            else:
                messages.error(request,'Your account is disabled')
                return render(request, template_name)
        else:
            messages.error(request,'Invalid login details')
            return render(request, template_name)

def Logout(request):
    logout(request)
    return redirect('/')

class AdminDashboard(View):
    def get(self, request, template_name='admindashboard.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

class Departments(View):
    def get(self, request, template_name='department.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            departments = Department.objects.all()
            message['departments']=departments
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

class AddDept(View):
    def get(self, request, template_name='add_department.html'):
        message={}
        try:
            print('kuchh mila1')
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            print('kuchh mila')
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

    def post(self, request, template_name='add_department.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            
            dept_name = request.POST.get('dept_name')
            building = request.POST.get('building')
            budget = request.POST.get('budget')
            
            if Department.objects.filter(dept_name=dept_name).exists():
                
                messages.error(request,'Department already exists. Try with diffirent name')
                return render(request,template_name,message)
            else:
                try:
                    
                    dept = Department(dept_name=dept_name,building=building,budget=int(budget))
                    dept.save()
                    messages.success(request,'Department added successfully.')
                    return redirect('Departments')
                except:
                    messages.error(request,'Something went wrong try again.')
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

def Del_dept(request,id):
    if request.method=='GET':
        try:
            to_del = Department.objects.get(dept_name=id)
            to_del.delete()
            messages.success(request,'Department Deleted')
        except:
            messages.error(request,'Something went wrong, try again.')

    return redirect('Departments')

class Classrooms(View):
    def get(self, request, template_name='classroom.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            classrooms = Classroom.objects.all()
            message['classrooms']=classrooms
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

class AddClassroom(View):
    def get(self, request, template_name='add_classroom.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

    def post(self, request, template_name='add_classroom.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            
            room_number = request.POST.get('room_number')
            building = request.POST.get('building')
            capacity = request.POST.get('capacity')
            
            
            try:
                dept = Classroom(room_number=room_number,building=building,capacity=int(capacity))
                dept.save()
                messages.success(request,'Classroom added successfully.')
                return redirect('Classrooms')
            except:
                messages.error(request,'Something went wrong try again.')
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

def Del_classroom(request,id):
    if request.method=='GET':
        try:
            to_del = Classroom.objects.get(id=id)
            to_del.delete()
            messages.success(request,'Classroom Deleted')
        except:
            messages.error(request,'Something went wrong, try again.')

    return redirect('Classrooms')

class Instructors(View):
    def get(self, request, template_name='instructor.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            instructors = Instructor.objects.all()
            message['instructors']=instructors
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

class AddInstructor(View):
    def get(self, request, template_name='add_instructor.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            departments = Department.objects.all()
            message['departments']=departments
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

    def post(self, request, template_name='add_instructor.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            departments = Department.objects.all()
            message['departments']=departments
            username = request.POST.get('username')
            password = request.POST.get('password')
            name = request.POST.get('name')
            salary = request.POST.get('salary')
            dept_name = request.POST.get('dept_name')
            
            
            try:
                dept_name = Department.objects.get(dept_name=dept_name)
                user = User(username=username,password=password)
                user.save()
                dept = Instructor(user=user,name=name,dept_name=dept_name,salary=int(salary))
                dept.save()
                messages.success(request,'Instructor added successfully.')
                return redirect('Instructors')
            except:
                messages.error(request,'Username already exists. Try with different username')
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

def Del_instructor(request,id):
    if request.method=='GET':
        try:
            to_del = Instructor.objects.get(id=id)
            to_del.delete()
            messages.success(request,'Instructor Deleted')
        except:
            messages.error(request,'Something went wrong, try again.')

    return redirect('Instructors')

class Students(View):
    def get(self, request, template_name='student.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            students = Student.objects.all()
            message['students']=students
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

class AddStudent(View):
    def get(self, request, template_name='add_student.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            departments = Department.objects.all()
            message['departments']=departments
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

    def post(self, request, template_name='add_student.html'):
        message={}
        try:
            this_admin = Portal_Admin.objects.get(user=request.user)
            message['admin']=this_admin
            departments = Department.objects.all()
            message['departments']=departments
            username = request.POST.get('username')
            password = request.POST.get('password')
            name = request.POST.get('name')
            tot_creds = request.POST.get('tot_creds')
            dept_name = request.POST.get('dept_name')
            
            
            try:
                dept_name = Department.objects.get(dept_name=dept_name)
                user = User(username=username,password=password)
                user.save()
                dept = Student(user=user,name=name,dept_name=dept_name,tot_creds=int(tot_creds))
                dept.save()
                messages.success(request,'Student added successfully.')
                return redirect('Students')
            except:
                messages.error(request,'Username already exists. Try with different username')
        except:
            messages.error(request,'Login to access the page')
            redirect('Login')
        return render(request,template_name,message)

def Del_student(request,id):
    if request.method=='GET':
        try:
            to_del = Student.objects.get(id=id)
            to_del.delete()
            messages.success(request,'Student Deleted')
        except:
            messages.error(request,'Something went wrong, try again.')

    return redirect('Students')
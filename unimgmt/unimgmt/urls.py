"""unimgmt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from university import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login.as_view(),name='Login'),
    path('logout/', views.Logout,name='Logout'),
    path('admin-dashboard/', views.AdminDashboard.as_view(),name='AdminDashboard'),
    path('admin-dashboard/department/', views.Departments.as_view(),name='Departments'),
    path('admin-dashboard/add-department/', views.AddDept.as_view(),name='AddDept'),
    path('del-dept/<str:id>/', views.Del_dept,name='Del_dept'),
    path('admin-dashboard/classroom/', views.Classrooms.as_view(),name='Classrooms'),
    path('admin-dashboard/add-classroom/', views.AddClassroom.as_view(),name='AddClassroom'),
    path('del-class/<str:id>/', views.Del_classroom,name='Del_classroom'),
    path('admin-dashboard/instructor/', views.Instructors.as_view(),name='Instructors'),
    path('admin-dashboard/add-instructor/', views.AddInstructor.as_view(),name='AddInstructor'),
    path('del-inst/<str:id>/', views.Del_instructor,name='Del_instructor'),
    path('admin-dashboard/student/', views.Students.as_view(),name='Students'),
    path('admin-dashboard/add-student/', views.AddStudent.as_view(),name='AddStudent'),
    path('del-stud/<str:id>/', views.Del_student,name='Del_student')
]

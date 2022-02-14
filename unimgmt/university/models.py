
from django.db.models import OneToOneField
from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE

# Create your models here.
class Portal_Admin(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=CASCADE)

    def __str__(self):
        return self.user.username


class Department(models.Model):
    dept_name = models.CharField(max_length=50,primary_key=True)
    building = models.CharField(max_length=50)
    budget = models.IntegerField()

    def __str__(self):
        return self.dept_name

class Course(models.Model):
    course_id = models.CharField(max_length=10,primary_key=True)
    title = models.CharField(max_length=50)
    dept_name = models.ForeignKey(Department,on_delete=SET_NULL,null=True)
    credits = models.IntegerField()

    def __str__(self):
        return self.course_id

class Prereq(models.Model):
    course_id = models.CharField(max_length=10,primary_key=True)
    prereq = models.ForeignKey(Course,on_delete=CASCADE)

    def __str__(self):
        return self.course_id

class Instructor(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    dept_name = models.ForeignKey(Department,on_delete=SET_NULL,null=True)
    salary = models.IntegerField()

    def __str__(self):
        return self.user.username

class Student(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    dept_name = models.ForeignKey(Department,on_delete=SET_NULL,null=True)
    tot_creds = models.IntegerField()

    def __str__(self):
        return self.user.username

class Advisor(models.Model):
    stud_id = models.ForeignKey(Student,primary_key=True,on_delete=CASCADE)
    inst_id = models.ForeignKey(Instructor,on_delete=CASCADE)

    def __str__(self):
        return self.stud_id + '-' + self.inst_id

DayChoices = [('Monday','Monday'),
              ('Tuesday','Tuesday'),
              ('Wednesday','Wednesday'),
              ('Thursday','Thursday'),
              ('Friday','Friday')
]

class TimeSlot(models.Model):
    time_slot_id = models.CharField(max_length=10,primary_key=True)
    day = models.CharField(choices=DayChoices,max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __str__(self):
        return self.time_slot_id

class Classroom(models.Model):
    building = models.CharField(max_length=50)
    room_number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return self.building + '-' + self.room_number

class Section(models.Model):
    course_id = models.ForeignKey(Course,on_delete=SET_NULL,null=True)
    sec_id = models.CharField(max_length=10,primary_key=True)
    semester = models.IntegerField()
    year = models.IntegerField()
    classroom = models.ForeignKey(Classroom,on_delete=SET_NULL,null=True)
    timeslot = models.ForeignKey(TimeSlot,on_delete=SET_NULL,null=True)

    def __str__(self):
        return self.sec_id

class Takes(models.Model):
    stud = models.ForeignKey(Student,on_delete=CASCADE)
    sec_id = models.ForeignKey(Section,on_delete=SET_NULL,null=True)
    grade = models.IntegerField(blank=True)

    def __str__(self):
        return self.stud

class Teaches(models.Model):
    teacher = models.ForeignKey(Instructor,on_delete=CASCADE)
    section = models.ForeignKey(Section,on_delete=CASCADE)

    def __str__(self):
        return self.teacher

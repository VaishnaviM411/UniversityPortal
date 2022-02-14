from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Portal_Admin)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Teaches)
admin.site.register(Takes)
admin.site.register(Classroom)
admin.site.register(Advisor)
admin.site.register(Section)
admin.site.register(TimeSlot)
admin.site.register(Prereq)
# Generated by Django 3.2.7 on 2022-02-13 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(max_length=50)),
                ('room_number', models.IntegerField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('building', models.CharField(max_length=50)),
                ('budget', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('dept_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('sec_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('year', models.IntegerField()),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.classroom')),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tot_creds', models.IntegerField()),
                ('dept_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('time_slot_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('day', models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday')], max_length=20)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Teaches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.section')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(blank=True)),
                ('sec_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.section')),
                ('stud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.student')),
            ],
        ),
        migrations.AddField(
            model_name='section',
            name='timeslot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.timeslot'),
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('course_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('prereq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.course')),
            ],
        ),
        migrations.CreateModel(
            name='Portal_Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dept_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='university.department'),
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='university.student')),
                ('inst_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.instructor')),
            ],
        ),
    ]
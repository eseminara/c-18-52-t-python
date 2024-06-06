from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Administrative'),
        ('parent', 'Parent'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=10, choices=ROLES)
    dni = models.CharField(max_length=20, unique=True, null=True, blank=True)
    address = models.CharField(max_length=90, null=True, blank=True)
    phone_number = models.CharField(max_length=25, unique=True, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Classroom(models.Model):
    name = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classrooms', limit_choices_to={'profile__role': 'teacher'})

    def __str__(self):
        return f'Curso: {self.name} - Profesor: {str(self.teacher)}'

class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments', limit_choices_to={'profile__role': 'student'})
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='enrollments')
    
    def __str__(self):
        return f'Alumno: {self.student} - Curso: {self.classroom} - Materia: {self.subject}'

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades', limit_choices_to={'profile__role': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    grade = models.DecimalField(max_digits=3, decimal_places=1)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Alumno: {self.student} - Materia: {self.subject} - Nota: {self.grade}'

class Event(models.Model):
    title = models.CharField(max_length=150, null=True)
    description = models.TextField()
    date = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    
    def __str__(self):
        return self.title + ' ' + str(self.date)

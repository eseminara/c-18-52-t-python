from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    ROLES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Administrative'),
        ('parent', 'Parent'),
    ]
    role = models.CharField(max_length=10, choices=ROLES)
    dni = models.CharField(max_length=20, unique=True, null=True, blank=True)
    address = models.CharField(max_length=90, null=True, blank=True)
    phone_number = models.CharField(max_length=25, unique=True, null=True, blank=True)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Avoid conflict with auth.User.groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Avoid conflict with auth.User.user_permissions
        blank=True
    )
     
    class Meta:
        unique_together = ('email', 'dni')
        
    def __str__(self):
        return self.username


class Classroom(models.Model):
    name = models.CharField(max_length=40, null=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classrooms', limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return f'Curso: {self.name} - Profesor: {str(self.teacher)}'

class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments', limit_choices_to={'role': 'student'})
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='enrollments')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='enrollments')
    
    def __str__(self):
        return f'Alumno: {self.student} - Curso: {self.classroom} - Materia: {self.subject}'

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades', limit_choices_to={'role': 'student'})
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    grade = models.DecimalField(max_digits=3, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Alumno: {self.student} - Materia: {self.subject} - Nota: {self.grade}'

class Event(models.Model):
    description = models.TextField()
    date = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    
    def __str__(self):
        return self.description

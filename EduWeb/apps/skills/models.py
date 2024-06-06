from django.db import models
from django.contrib.auth.models import User
from apps.users.models import UserProfile

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class StudentSkill(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_skills', limit_choices_to={'profile__role': 'student'})
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='student_skills')
    level = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f'{self.student.username} - {self.skill.name} - {self.level}'


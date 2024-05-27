from django.contrib import admin

# Register your models here.
from .models import User, Classroom, Subject, Enrollment, Grade, Event

admin.site.register(User)
admin.site.register(Classroom)
admin.site.register(Subject)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Event)

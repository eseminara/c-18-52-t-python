from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import User, Classroom, Subject, Enrollment, Grade, Event
from .serializers import UserSerializer, ClassroomSerializer, SubjectSerializer, EnrollmentSerializer, GradeSerializer, EventSerializer


@api_view(['GET', 'POST'])
def custom_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'logged_in.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

@api_view(['POST'])
def custom_logout(request):
    logout(request)
    return redirect('custom_login')







class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

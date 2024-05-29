from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ClassroomViewSet, SubjectViewSet, EnrollmentViewSet, GradeViewSet, EventViewSet, custom_login, custom_logout

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', custom_login, name='custom_login'),
    path('logout/', custom_logout, name='custom_logout'),
]

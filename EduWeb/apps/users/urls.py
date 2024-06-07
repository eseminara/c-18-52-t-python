from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomLoginView, CustomLogoutView, UserViewSet, ClassroomViewSet, SubjectViewSet, EnrollmentViewSet, GradeViewSet, EventViewSet, UserProfileView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'events', EventViewSet)




urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='custom_login'),
    path('logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('', include(router.urls))
    
]
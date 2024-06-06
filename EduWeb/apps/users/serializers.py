from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, Classroom, Subject, Enrollment, Grade, Event

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'role', 'dni', 'address', 'phone_number',
            'parent_name', 'parent_phone', 'parent_email'
        ]

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()

        profile.role = profile_data.get('role', profile.role)
        profile.dni = profile_data.get('dni', profile.dni)
        profile.address = profile_data.get('address', profile.address)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.parent_name = profile_data.get('parent_name', profile.parent_name)
        profile.parent_phone = profile_data.get('parent_phone', profile.parent_phone)
        profile.parent_email = profile_data.get('parent_email', profile.parent_email)
        profile.save()

        return instance

class EnrollmentSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    subject = serializers.StringRelatedField()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'subject']

class ClassroomSerializer(serializers.ModelSerializer):
    teacher = UserSerializer()
    enrollments = EnrollmentSerializer(many=True, read_only=True)
    date_joined = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model = Classroom
        fields = ['id', 'name', 'description', 'date_joined', 'teacher', 'enrollments']

class SubjectSerializer(serializers.ModelSerializer):
    enrollments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    grades = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'description', 'date_joined', 'enrollments', 'grades']

class GradeSerializer(serializers.ModelSerializer):
    student = UserSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Grade
        fields = ['id', 'student', 'subject', 'grade', 'date']

class EventSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    date_joined = serializers.DateTimeField(format="%d-%m-%Y %H:%M")
    date = serializers.DateTimeField(format="%d-%m-%Y %H:%M")

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'date_joined', 'created_by']

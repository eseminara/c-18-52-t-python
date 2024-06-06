from rest_framework import serializers
from django.contrib.auth.models import User
from apps.users.serializers import UserSerializer
from .models import Skill, StudentSkill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class StudentSkillSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(profile__role='student'))
    skill = SkillSerializer()

    class Meta:
        model = StudentSkill
        fields = ['id', 'student', 'skill', 'level']

    def create(self, validated_data):
        skill_data = validated_data.pop('skill')
        skill, created = Skill.objects.get_or_create(**skill_data)
        student_skill = StudentSkill.objects.create(skill=skill, **validated_data)
        return student_skill

    def update(self, instance, validated_data):
        skill_data = validated_data.pop('skill')
        skill, created = Skill.objects.get_or_create(**skill_data)

        instance.student = validated_data.get('student', instance.student)
        instance.skill = skill
        instance.level = validated_data.get('level', instance.level)
        instance.save()
        return instance

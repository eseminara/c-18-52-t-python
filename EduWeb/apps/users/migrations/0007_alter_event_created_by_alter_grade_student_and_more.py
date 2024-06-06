# Generated by Django 5.0.6 on 2024-06-05 06:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forum_author_alter_message_author'),
        ('users', '0006_event_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(limit_choices_to={'profile__role': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='grades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(limit_choices_to={'profile__role': 'teacher'}, on_delete=django.db.models.deletion.CASCADE, related_name='classrooms', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='student',
            field=models.ForeignKey(limit_choices_to={'profile__role': 'student'}, on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('admin', 'Administrative'), ('parent', 'Parent')], max_length=10)),
                ('dni', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('address', models.CharField(blank=True, max_length=90, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=25, null=True, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

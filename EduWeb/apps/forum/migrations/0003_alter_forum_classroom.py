# Generated by Django 5.0.6 on 2024-06-05 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forum_author_alter_message_author'),
        ('users', '0010_alter_grade_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='users.classroom'),
        ),
    ]

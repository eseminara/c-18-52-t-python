# Generated by Django 5.0.6 on 2024-05-27 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_grade_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='name',
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]

# Generated by Django 5.0 on 2023-12-18 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_is_active_alter_customuser_is_staff_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
    ]

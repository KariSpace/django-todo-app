# Generated by Django 3.1.7 on 2022-08-14 12:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo_list', '0002_auto_20220814_1216'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tack',
            new_name='Task',
        ),
    ]

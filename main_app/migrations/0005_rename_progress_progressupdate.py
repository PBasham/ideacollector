# Generated by Django 4.0.4 on 2022-07-22 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_progress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Progress',
            new_name='ProgressUpdate',
        ),
    ]

# Generated by Django 4.0.4 on 2022-07-22 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='idea',
            old_name='tag',
            new_name='tags',
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-04 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EnsPost', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-27 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnsPost', '0002_auto_20200119_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

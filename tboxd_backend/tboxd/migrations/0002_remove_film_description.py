# Generated by Django 4.0.2 on 2022-02-02 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tboxd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='description',
        ),
    ]

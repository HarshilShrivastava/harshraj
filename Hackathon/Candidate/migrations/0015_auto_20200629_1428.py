# Generated by Django 3.0.2 on 2020-06-29 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0014_auto_20200629_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialmedia',
            old_name='Socialmedia',
            new_name='name',
        ),
    ]
# Generated by Django 3.0.2 on 2020-08-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organization', '0016_auto_20200730_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Address',
            field=models.TextField(max_length=50),
        ),
    ]

# Generated by Django 3.0.2 on 2020-07-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0023_jobenquiryc_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobenquiryc',
            name='similarity',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.0.2 on 2020-07-13 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0018_auto_20200713_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='Recruit',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='Candidate.Recruit'),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.0.2 on 2020-06-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0015_auto_20200629_1428'),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='SocialMediaTags',
            field=models.ManyToManyField(blank=True, to='Candidate.SocialMediaTags'),
        ),
        migrations.AddField(
            model_name='blogs',
            name='SocioeconomicTags',
            field=models.ManyToManyField(blank=True, to='Candidate.SocioeconomicTags'),
        ),
        migrations.AddField(
            model_name='courses',
            name='SocialMediaTags',
            field=models.ManyToManyField(blank=True, to='Candidate.SocialMediaTags'),
        ),
        migrations.AddField(
            model_name='courses',
            name='SocioeconomicTags',
            field=models.ManyToManyField(blank=True, to='Candidate.SocioeconomicTags'),
        ),
    ]
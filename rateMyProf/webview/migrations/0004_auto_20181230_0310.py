# Generated by Django 2.1.4 on 2018-12-30 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0003_finalratings_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalratings',
            name='numAttendance',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='finalratings',
            name='numGrade',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='finalratings',
            name='numTa',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='finalratings',
            name='numTiming',
            field=models.IntegerField(default=1),
        ),
    ]

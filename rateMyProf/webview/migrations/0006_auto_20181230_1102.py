# Generated by Django 2.1.4 on 2018-12-30 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webview', '0005_auto_20181230_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='departmentCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='professor',
            name='designation',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='professor',
            name='name',
            field=models.CharField(max_length=75),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=75),
        ),
    ]
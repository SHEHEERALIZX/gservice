# Generated by Django 2.2.7 on 2020-06-07 07:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tc', '0005_tcapplication_dateofremovedfromrolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcapplication',
            name='dateofApplication',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tcapplication',
            name='lastAttendedDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tcapplication',
            name='promotionDate',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='tcapplication',
            name='tcNumber',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tcapplication',
            name='tcYear',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='tcapplication',
            name='tc_application_Number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tcapplication',
            name='tc_application_Year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
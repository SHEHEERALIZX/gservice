# Generated by Django 2.2.7 on 2020-04-08 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(default='CM', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
                ('academicyear', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_tools.AcademicSession')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_tools.Department')),
            ],
            options={
                'ordering': ['department', 'semester'],
                'unique_together': {('academicyear', 'department', 'semester')},
            },
        ),
    ]

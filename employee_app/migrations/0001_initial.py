# Generated by Django 3.1.2 on 2020-11-05 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designationName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizationName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_app.userprofile')),
                ('department', models.ManyToManyField(related_name='emp', to='employee_app.Department')),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='employee_app.designation')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_app.organization'),
        ),
    ]

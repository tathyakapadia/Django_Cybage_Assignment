# Generated by Django 3.1.2 on 2020-10-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0004_auto_20201014_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
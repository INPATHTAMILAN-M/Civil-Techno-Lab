# Generated by Django 4.2.7 on 2024-01-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_employee_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='joining_date',
            field=models.DateTimeField(),
        ),
    ]

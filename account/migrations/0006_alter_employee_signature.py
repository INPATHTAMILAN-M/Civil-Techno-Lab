# Generated by Django 4.2.7 on 2024-01-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_employee_signature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='signature',
            field=models.ImageField(blank=True, null=True, upload_to='signature'),
        ),
    ]

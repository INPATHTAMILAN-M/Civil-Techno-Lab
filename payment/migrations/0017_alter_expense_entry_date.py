# Generated by Django 4.2.7 on 2024-01-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0016_alter_invoice_test_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense_entry',
            name='date',
            field=models.DateTimeField(),
        ),
    ]

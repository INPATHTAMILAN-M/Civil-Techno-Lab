# Generated by Django 4.2.7 on 2024-01-20 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0018_invoice_file_expense_invoice_test_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice_file',
            name='expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.expense_entry'),
        ),
    ]

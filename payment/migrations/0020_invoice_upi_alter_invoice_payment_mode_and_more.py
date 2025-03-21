# Generated by Django 4.2.7 on 2024-01-22 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_alter_invoice_file_expense'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='upi',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI')], max_length=6),
        ),
    ]

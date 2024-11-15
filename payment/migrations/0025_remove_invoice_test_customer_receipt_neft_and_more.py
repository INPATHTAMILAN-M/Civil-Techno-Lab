# Generated by Django 4.2.7 on 2024-03-29 08:30

from django.db import migrations, models
import payment.models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0024_invoice_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice_test',
            name='customer',
        ),
        migrations.AddField(
            model_name='receipt',
            name='neft',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('neft', 'NEFT')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='invoice_file',
            name='file',
            field=models.FileField(upload_to=payment.models.wrapper),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('neft', 'NEFT')], max_length=6),
        ),
    ]

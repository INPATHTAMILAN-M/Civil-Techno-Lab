# Generated by Django 4.2.7 on 2024-07-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0026_invoice_tds_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='tds',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('neft', 'NEFT'), ('tds', 'TDS')], max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='payment_mode',
            field=models.CharField(choices=[('cash', 'Cash'), ('cheque', 'Cheque'), ('upi', 'UPI'), ('neft', 'NEFT'), ('tds', 'TDS')], max_length=6),
        ),
    ]
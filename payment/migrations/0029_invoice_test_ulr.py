# Generated by Django 4.2.7 on 2024-11-14 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0028_invoice_test_is_authorised_signatory'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_test',
            name='ulr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

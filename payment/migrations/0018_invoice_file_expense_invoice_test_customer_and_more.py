# Generated by Django 4.2.7 on 2024-01-20 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_employee_email'),
        ('general', '0004_alter_material_template'),
        ('payment', '0017_alter_expense_entry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_file',
            name='expense',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='general.expense'),
        ),
        migrations.AddField(
            model_name='invoice_test',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.customer'),
        ),
        migrations.AlterField(
            model_name='invoice_test',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.invoice'),
        ),
    ]

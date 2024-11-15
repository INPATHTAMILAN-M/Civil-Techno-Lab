# Generated by Django 4.2.7 on 2024-01-03 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment', '0002_alter_expense_entry_expense_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense_entry',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense_entry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='expense_entry',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expense_entry',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice_file',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invoice_file_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice_file',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice_file',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='invoice_file',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]

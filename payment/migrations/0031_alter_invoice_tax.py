# Generated by Django 4.2.7 on 2024-12-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_alter_material_template'),
        ('payment', '0030_invoice_is_old_invoice_format'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='tax',
            field=models.ManyToManyField(blank=True, to='general.tax'),
        ),
    ]

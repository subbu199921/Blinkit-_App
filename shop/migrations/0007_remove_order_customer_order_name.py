# Generated by Django 5.1.7 on 2025-03-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_order_name_order_amount_order_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]

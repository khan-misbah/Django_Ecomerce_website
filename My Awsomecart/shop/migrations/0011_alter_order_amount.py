# Generated by Django 4.1.7 on 2023-05-01 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.CharField(default=0, max_length=500),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shopitems_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopitems',
            name='stock',
            field=models.IntegerField(default=1),
        ),
    ]

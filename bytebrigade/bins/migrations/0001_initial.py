# Generated by Django 4.1.7 on 2023-03-16 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BinData',
            fields=[
                ('binId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('binName', models.CharField(default='bin', max_length=100)),
                ('binLat', models.DecimalField(decimal_places=22, max_digits=100)),
                ('binLong', models.DecimalField(decimal_places=22, max_digits=100)),
                ('binPhoto', models.ImageField(default='figures/bins/default.jpg', upload_to='')),
                ('bin_general', models.BooleanField(default=False)),
                ('bin_recycle', models.BooleanField(default=False)),
                ('bin_paper', models.BooleanField(default=False)),
                ('bin_cans', models.BooleanField(default=False)),
                ('bin_glass', models.BooleanField(default=False)),
                ('bin_plastic', models.BooleanField(default=False)),
                ('bin_non_rec', models.BooleanField(default=False)),
            ],
        ),
    ]

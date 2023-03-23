# Generated by Django 4.1.7 on 2023-03-16 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('goalID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('target', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='UserGoal',
            fields=[
                ('userGoalID', models.AutoField(primary_key=True, serialize=False)),
                ('userGoalNum', models.IntegerField()),
                ('value', models.DecimalField(decimal_places=5, max_digits=10)),
                ('goalType', models.CharField(choices=[('Recycling', 'Recycling'), ('Plastic', 'Plastic'), ('Paper', 'Paper'), ('Cans', 'Cans'), ('Glass', 'Glass')], default='Recycling', max_length=25)),
                ('goal', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='account.goal')),
                ('user', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('carbon', models.FloatField(default=0)),
                ('curweek', models.FloatField(default=0)),
                ('curmonth', models.FloatField(default=0)),
                ('curyear', models.FloatField(default=0)),
                ('lastRecycle', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='lastRecycle', to='products.product')),
                ('loveRecycling', models.ForeignKey(default='1', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='loveRecycle', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
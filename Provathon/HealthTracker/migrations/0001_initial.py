# Generated by Django 3.2.5 on 2021-07-15 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.IntegerField()),
                ('chestpain', models.IntegerField()),
                ('angina', models.IntegerField()),
                ('slope', models.IntegerField()),
                ('thalassemia', models.IntegerField()),
                ('heartbeats', models.IntegerField()),
                ('cholestorol', models.FloatField()),
                ('major_vessels', models.IntegerField()),
                ('st_depression', models.FloatField()),
                ('blood_pressure', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskPercentange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128)),
                ('value', models.FloatField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risk', related_query_name='risk', to='HealthTracker.patient')),
            ],
        ),
    ]

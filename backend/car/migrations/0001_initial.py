# Generated by Django 4.0.1 on 2022-01-22 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=250)),
                ('registration_code', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 5.0.7 on 2024-07-18 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roulettech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
            ],
        ),
    ]

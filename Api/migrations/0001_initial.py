# Generated by Django 3.1.1 on 2020-12-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField(unique=True)),
                ('city', models.CharField(max_length=100)),
                ('marks', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(choices=[('Regular', 'Regular'), ('Square', 'Square')], max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]

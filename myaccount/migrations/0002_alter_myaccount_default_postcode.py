# Generated by Django 3.2 on 2021-05-31 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaccount',
            name='default_postcode',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]

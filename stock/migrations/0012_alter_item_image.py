# Generated by Django 3.2 on 2021-04-26 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0011_auto_20210426_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='SOME STRING', upload_to=''),
        ),
    ]
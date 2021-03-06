# Generated by Django 3.2 on 2021-05-15 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0001_initial'),
        ('checkout', '0002_auto_20210512_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='my_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myaccount.myaccount'),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='country',
            field=models.CharField(max_length=50),
        ),
    ]

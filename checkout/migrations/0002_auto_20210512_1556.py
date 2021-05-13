# Generated by Django 3.2 on 2021-05-12 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkout',
            old_name='address1',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='checkout',
            old_name='lastname',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='checkout_items',
            old_name='item_total',
            new_name='items_total',
        ),
        migrations.AddField(
            model_name='checkout',
            name='city',
            field=models.CharField(default='CITY', max_length=20),
        ),
        migrations.AlterField(
            model_name='checkout_items',
            name='checkout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkoutitems', to='checkout.checkout'),
        ),
    ]
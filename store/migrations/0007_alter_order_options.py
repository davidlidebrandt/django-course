# Generated by Django 4.0.4 on 2022-05-11 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_cart_id_alter_cartitem_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'permissions': [('cancel_order', 'Can cancel order')]},
        ),
    ]

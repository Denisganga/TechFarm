# Generated by Django 4.2.1 on 2023-06-10 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_alter_machinery_purchase_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machinery',
            name='number_plate',
            field=models.CharField(max_length=20),
        ),
    ]
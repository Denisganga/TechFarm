# Generated by Django 4.2.1 on 2023-06-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0010_remove_expenses_id_alter_expenses_eid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('Rid', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('the_field', models.TextField()),
                ('the_report', models.TextField()),
            ],
        ),
    ]

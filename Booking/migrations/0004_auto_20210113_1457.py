# Generated by Django 3.1.5 on 2021-01-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0003_auto_20210113_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(help_text='Pizza caption', max_length=64),
        ),
    ]
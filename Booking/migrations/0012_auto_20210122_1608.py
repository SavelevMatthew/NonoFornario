# Generated by Django 3.1.5 on 2021-01-22 16:08

import Booking.booking_functions.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0011_auto_20210122_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(help_text='Day of the order', validators=[Booking.booking_functions.validators.future_date_check]),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-22 16:32

import Booking.booking_functions.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0012_auto_20210122_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time_from',
            field=models.TimeField(help_text='Reservation start (min-val: 18:00)', validators=[Booking.booking_functions.validators.start_time_check]),
        ),
        migrations.AlterField(
            model_name='booking',
            name='time_to',
            field=models.TimeField(help_text='Reservation end (max-val: 23:59)', validators=[Booking.booking_functions.validators.start_time_check]),
        ),
    ]

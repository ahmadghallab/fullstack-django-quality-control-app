# Generated by Django 2.0.6 on 2018-07-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0030_auto_20180716_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketevaluation',
            name='ticket_number',
            field=models.IntegerField(default=0),
        ),
    ]

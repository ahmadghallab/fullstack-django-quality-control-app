# Generated by Django 2.0.6 on 2018-06-10 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_auto_20180610_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yesornoresult',
            name='yes_or_no',
            field=models.IntegerField(),
        ),
    ]

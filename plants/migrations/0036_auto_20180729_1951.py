# Generated by Django 2.0.6 on 2018-07-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0035_auto_20180729_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='telephone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
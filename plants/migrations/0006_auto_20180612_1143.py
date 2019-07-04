# Generated by Django 2.0.6 on 2018-06-12 11:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_auto_20180610_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='yesornoresult',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='yesornoresult',
            name='yes_or_no',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
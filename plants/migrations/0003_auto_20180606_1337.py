# Generated by Django 2.0.6 on 2018-06-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_auto_20180602_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='place',
        ),
        migrations.AlterField(
            model_name='place',
            name='ar_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='en_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together={('place', 'en_name')},
        ),
    ]

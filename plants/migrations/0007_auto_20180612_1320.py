# Generated by Django 2.0.6 on 2018-06-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0006_auto_20180612_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='yesornoresult',
            name='notes',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='yesornoresult',
            name='yes_or_no',
            field=models.IntegerField(default=0),
        ),
    ]

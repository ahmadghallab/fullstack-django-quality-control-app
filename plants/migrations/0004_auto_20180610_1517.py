# Generated by Django 2.0.6 on 2018-06-10 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_auto_20180606_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='YesOrNoResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yes_or_no', models.CharField(max_length=3)),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_criteria', to='plants.Criteria')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='department',
            name='ar_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='en_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='yesornoresult',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_department', to='plants.Department'),
        ),
        migrations.AddField(
            model_name='yesornoresult',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_employee', to='plants.Employee'),
        ),
        migrations.AddField(
            model_name='yesornoresult',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='result_place', to='plants.Place'),
        ),
    ]

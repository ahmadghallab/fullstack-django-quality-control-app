# Generated by Django 2.0.6 on 2018-06-25 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0010_auto_20180625_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='criteria',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='department',
        ),
        migrations.RemoveField(
            model_name='yesornoresult',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.AddField(
            model_name='criteria',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='criteria_department', to='plants.Major'),
        ),
        migrations.AddField(
            model_name='employee',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employee_department', to='plants.Major'),
        ),
        migrations.AddField(
            model_name='yesornoresult',
            name='major',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='result_department', to='plants.Major'),
        ),
    ]
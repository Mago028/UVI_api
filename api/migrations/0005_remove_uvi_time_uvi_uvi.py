# Generated by Django 4.2.1 on 2023-06-07 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_area_no_uvi_areano'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uvi',
            name='time',
        ),
        migrations.AddField(
            model_name='uvi',
            name='UVI',
            field=models.IntegerField(default=0),
        ),
    ]
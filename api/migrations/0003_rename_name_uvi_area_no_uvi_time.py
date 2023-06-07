# Generated by Django 4.2.1 on 2023-06-07 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_beach_uvi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uvi',
            old_name='name',
            new_name='area_no',
        ),
        migrations.AddField(
            model_name='uvi',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
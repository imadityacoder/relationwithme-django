# Generated by Django 5.0 on 2023-12-13 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='relation',
            new_name='rel',
        ),
        migrations.AddField(
            model_name='relation',
            name='date',
            field=models.DateField(default=None),
        ),
    ]

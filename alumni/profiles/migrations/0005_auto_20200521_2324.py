# Generated by Django 3.0.5 on 2020-05-21 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profilecareerhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledegrees',
            name='year_graduated',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profiledegrees',
            name='year_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]

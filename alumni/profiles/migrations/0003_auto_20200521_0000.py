# Generated by Django 3.0.5 on 2020-05-21 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profiledegrees'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiledegrees',
            old_name='name',
            new_name='institution_name',
        ),
    ]

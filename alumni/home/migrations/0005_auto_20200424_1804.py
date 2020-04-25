# Generated by Django 3.0.5 on 2020-04-24 18:04

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200424_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'AlumniShip', 'verbose_name_plural': 'AlumniShips'},
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='banner_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-19 03:27

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0005_auto_20200519_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='institutionlistingpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
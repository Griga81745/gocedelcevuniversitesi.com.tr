# Generated by Django 4.1.1 on 2022-09-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0011_sitesettings_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Site Açıklaması'),
        ),
    ]
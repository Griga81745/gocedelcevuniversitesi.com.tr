# Generated by Django 4.1.1 on 2022-09-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0010_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='description',
            field=models.TextField(blank=True,null=True,default=None, verbose_name='Site Açıklaması'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0006_request_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='slide/', verbose_name='Resim')),
            ],
        ),
        migrations.DeleteModel(
            name='Faculty',
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-28 17:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='')),
            ],
            options={
                'verbose_name': 'İl',
                'verbose_name_plural': 'İller',
            },
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'Bölüm', 'verbose_name_plural': 'Bölümler'},
        ),
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Fakülte', 'verbose_name_plural': 'Fakülteler'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Sıkça Sorulan Soru', 'verbose_name_plural': 'Sıkça Sorulan Sorular'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Haber', 'verbose_name_plural': 'Haberler'},
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ad')),
                ('tc', models.IntegerField(verbose_name='T.C. Numarası')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Telefon Numarası')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.area', verbose_name='Bölüm')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.city', verbose_name='İl')),
            ],
            options={
                'verbose_name': 'Başvuru',
                'verbose_name_plural': 'Başvurular',
            },
        ),
    ]

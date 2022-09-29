# Generated by Django 4.1.1 on 2022-09-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('price', models.IntegerField(verbose_name='Fiyat?')),
                ('continuance', models.IntegerField(verbose_name='Kaç Yıl?')),
                ('language', models.CharField(max_length=255, verbose_name='Dil')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Soru')),
                ('content', models.TextField(verbose_name='Cevap')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('image', models.ImageField(upload_to='posts/', verbose_name='Resim')),
                ('content', models.TextField(verbose_name='İçerik')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Başlık')),
                ('image', models.ImageField(upload_to='faculties/', verbose_name='Resim')),
                ('areas', models.ManyToManyField(related_name='areas', to='university.area', verbose_name='Bölümler')),
            ],
        ),
    ]
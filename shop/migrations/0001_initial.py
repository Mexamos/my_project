# Generated by Django 2.2.2 on 2019-07-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='gallery', verbose_name='Изображение')),
                ('price', models.FloatField(blank=True, null=True, verbose_name='Цена')),
            ],
            options={
                'ordering': ['-name'],
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0002_advertisement_date_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='category',
            field=models.CharField(choices=[('TK', 'Танки'), ('HL', 'Хилы'), ('DD', 'ДД'), ('TM', 'Торговцы'), ('GM', 'Гилдмастеры'), ('QG', 'Квестгиверы'), ('BM', 'Кузнецы'), ('TN', 'Кожевники'), ('PM', 'Зельевары'), ('IM', 'Мастера заклинаний')], max_length=2),
        ),
    ]

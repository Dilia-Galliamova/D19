# Generated by Django 4.1.7 on 2023-03-14 18:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0004_reply_status_alter_advertisement_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст'),
        ),
    ]

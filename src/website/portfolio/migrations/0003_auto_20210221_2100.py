# Generated by Django 3.1.7 on 2021-02-22 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210221_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.FilePathField(),
        ),
    ]

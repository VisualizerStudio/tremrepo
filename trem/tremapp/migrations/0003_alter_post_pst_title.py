# Generated by Django 3.2.13 on 2022-07-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tremapp', '0002_auto_20220725_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pst_title',
            field=models.CharField(max_length=40, verbose_name='Title'),
        ),
    ]

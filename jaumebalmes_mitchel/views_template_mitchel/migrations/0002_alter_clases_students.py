# Generated by Django 4.2.2 on 2023-06-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('views_template_mitchel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clases',
            name='students',
            field=models.IntegerField(),
        ),
    ]

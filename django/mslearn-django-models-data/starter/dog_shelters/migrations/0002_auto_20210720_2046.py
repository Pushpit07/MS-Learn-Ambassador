# Generated by Django 3.2.5 on 2021-07-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_shelters', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='adoption_date',
        ),
        migrations.AlterField(
            model_name='dog',
            name='description',
            field=models.TextField(),
        ),
    ]

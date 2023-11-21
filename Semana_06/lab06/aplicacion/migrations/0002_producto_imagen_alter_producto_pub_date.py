# Generated by Django 4.2.5 on 2023-10-03 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
# Generated by Django 2.2.4 on 2019-12-23 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalpublication',
            name='journal',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='journal',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]

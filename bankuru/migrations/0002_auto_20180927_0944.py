# Generated by Django 2.0.6 on 2018-09-27 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankuru', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='debt',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]

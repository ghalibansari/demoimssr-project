# Generated by Django 2.1.2 on 2018-10-03 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='proname',
            new_name='Lab_incharge_name',
        ),
    ]
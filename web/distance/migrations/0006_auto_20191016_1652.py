# Generated by Django 2.2.5 on 2019-10-16 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('distance', '0005_auto_20191016_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cords',
            old_name='user_name',
            new_name='name',
        ),
    ]
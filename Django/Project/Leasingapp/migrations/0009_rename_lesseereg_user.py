# Generated by Django 4.1.2 on 2022-10-28 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leasingapp', '0008_rename_lessorreg_lessor'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='lesseereg',
            new_name='user',
        ),
    ]
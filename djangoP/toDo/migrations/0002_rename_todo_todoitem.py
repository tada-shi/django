# Generated by Django 3.2.5 on 2021-07-18 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toDo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='toDO',
            new_name='toDOItem',
        ),
    ]

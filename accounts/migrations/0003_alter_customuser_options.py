# Generated by Django 4.1.6 on 2023-02-01 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('first_name',)},
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-07 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kewayy_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='number_of_test_cases',
        ),
    ]

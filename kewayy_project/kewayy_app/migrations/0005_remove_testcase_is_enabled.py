# Generated by Django 2.2.5 on 2019-09-19 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kewayy_app', '0004_auto_20190908_0418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testcase',
            name='is_enabled',
        ),
    ]

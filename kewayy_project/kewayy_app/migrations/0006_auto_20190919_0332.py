# Generated by Django 2.2.5 on 2019-09-19 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kewayy_app', '0005_remove_testcase_is_enabled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='has_passed',
            field=models.NullBooleanField(default=False),
        ),
    ]

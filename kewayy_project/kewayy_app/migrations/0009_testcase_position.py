# Generated by Django 2.2.5 on 2019-09-23 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kewayy_app', '0008_auto_20190922_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kewayy_app', '0006_auto_20190919_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='has_passed',
            field=models.NullBooleanField(),
        ),
    ]

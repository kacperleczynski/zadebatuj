# Generated by Django 3.0.5 on 2020-05-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksm_app', '0002_auto_20200503_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debatantsbattle',
            name='data',
            field=models.CharField(max_length=256),
        ),
    ]

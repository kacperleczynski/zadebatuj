# Generated by Django 3.0.5 on 2020-05-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksm_app', '0019_auto_20200514_0551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='judges',
            name='discord',
        ),
        migrations.RemoveField(
            model_name='judges',
            name='zoom',
        ),
        migrations.AddField(
            model_name='debatants',
            name='facebook',
            field=models.URLField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='debatants',
            name='opis',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='debatants',
            name='terminy',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='judges',
            name='facebook',
            field=models.URLField(max_length=256, null=True),
        ),
    ]
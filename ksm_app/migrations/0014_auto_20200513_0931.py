# Generated by Django 3.0.5 on 2020-05-13 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ksm_app', '0013_auto_20200510_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='debatants',
            options={'ordering': ['imię']},
        ),
        migrations.AlterModelOptions(
            name='judges',
            options={'ordering': ['imię']},
        ),
        migrations.AddField(
            model_name='debatantsbattle',
            name='godzina',
            field=models.TimeField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='debatantsbattle',
            name='data',
            field=models.DateField(max_length=256, null=True),
        ),
    ]

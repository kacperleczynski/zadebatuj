# Generated by Django 3.0.5 on 2020-05-10 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ksm_app', '0010_auto_20200510_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debatantsbattle',
            name='user1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user1', to='ksm_app.Debatants'),
        ),
        migrations.AlterField(
            model_name='debatantsbattle',
            name='user2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user2', to='ksm_app.Debatants'),
        ),
    ]

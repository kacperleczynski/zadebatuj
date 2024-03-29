# Generated by Django 3.0.5 on 2020-05-03 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ksm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DebatantsBattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('transmisja', models.URLField()),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ksm_app.Judges')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user1', to='ksm_app.Debatants')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user2', to='ksm_app.Debatants')),
            ],
        ),
        migrations.DeleteModel(
            name='Battle',
        ),
    ]

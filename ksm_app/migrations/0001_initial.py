# Generated by Django 3.0.5 on 2020-05-03 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Judges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=256)),
                ('nazwisko', models.CharField(max_length=256)),
                ('miasto', models.CharField(max_length=256)),
                ('szkoła', models.CharField(max_length=256)),
                ('organizacja', models.CharField(max_length=256)),
                ('zoom', models.URLField(max_length=256)),
                ('discord', models.URLField(max_length=256)),
                ('dyspozycyjnosc', models.TextField(max_length=1000)),
                ('opis', models.TextField(max_length=2000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Debatants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imię', models.CharField(max_length=256)),
                ('nazwisko', models.CharField(max_length=256)),
                ('miasto', models.CharField(max_length=256)),
                ('szkoła', models.CharField(max_length=256)),
                ('organizacja', models.CharField(max_length=256)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('transmisja', models.URLField()),
                ('judge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ksm_app.Judges')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user1', to='ksm_app.Debatants')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user2', to='ksm_app.Debatants')),
            ],
        ),
    ]
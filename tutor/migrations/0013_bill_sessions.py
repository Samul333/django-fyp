# Generated by Django 3.1.7 on 2021-04-12 13:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0012_auto_20210411_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=40)),
                ('session_date', models.DateField(default=datetime.date(2021, 4, 12))),
                ('session_time', models.TimeField(default=datetime.time(13, 23, 24, 93454))),
                ('session_duration', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tutro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Payment_type', models.CharField(max_length=30)),
                ('session_cost', models.IntegerField(default=0)),
                ('seession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.sessions')),
            ],
        ),
    ]
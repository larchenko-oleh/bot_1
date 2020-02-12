# Generated by Django 3.0.2 on 2020-01-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ViberUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=128)),
                ('viber_id', models.CharField(max_length=24)),
                ('country', models.CharField(max_length=2)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('is_blocked', models.BooleanField(blank=True, null=True)),
                ('api_version', models.PositiveSmallIntegerField()),
            ],
        ),
    ]

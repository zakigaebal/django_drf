# Generated by Django 4.1.1 on 2022-09-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(default='identify', max_length=20)),
                ('password', models.CharField(default='password', max_length=20)),
            ],
        ),
    ]

# Generated by Django 2.0 on 2017-12-11 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evrytesttools', '0004_auto_20171207_0326'),
    ]

    operations = [
        migrations.CreateModel(
            name='QueryCMDBRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('hostname', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('memorysize', models.CharField(max_length=100)),
                ('tshirtsize', models.CharField(max_length=100)),
                ('numcpus', models.CharField(max_length=100)),
                ('operationalstatus', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('-name', '-date'),
            },
        ),
    ]

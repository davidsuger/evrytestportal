# Generated by Django 2.0 on 2017-12-11 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evrytesttools', '0005_querycmdbrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='SRCreateServerLinuxRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True, auto_now=True)),
                ('item', models.CharField(max_length=100)),
                ('customer', models.CharField(max_length=100)),
                ('customername', models.CharField(max_length=100)),
                ('disasterlevelclass', models.CharField(max_length=100)),
                ('hostname', models.CharField(max_length=100)),
                ('operationsystem', models.CharField(max_length=100)),
                ('environment', models.CharField(max_length=100)),
                ('backup', models.CharField(max_length=100)),
                ('servicelevel', models.CharField(max_length=100)),
                ('servicemodel', models.CharField(max_length=100)),
                ('retentionofbackup', models.CharField(max_length=100)),
                ('storegetier', models.CharField(max_length=100)),
                ('serverbemanaged', models.CharField(max_length=100)),
                ('hypervisor', models.CharField(max_length=100)),
                ('securityzone', models.CharField(max_length=100)),
                ('tshirtsize', models.CharField(max_length=100)),
                ('vcpusize', models.CharField(max_length=100)),
                ('memsize', models.CharField(max_length=100)),
                ('srsubmitedinfo', models.CharField(max_length=300)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]

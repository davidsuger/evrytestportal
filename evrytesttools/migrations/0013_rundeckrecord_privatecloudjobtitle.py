# Generated by Django 2.0 on 2017-12-28 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('evrytesttools', '0012_rundeckrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='rundeckrecord',
            name='privatecloudJobTitle',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
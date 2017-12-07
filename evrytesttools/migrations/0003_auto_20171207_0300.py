# Generated by Django 2.0 on 2017-12-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evrytesttools', '0002_querysrrecords'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='querysrrecords',
            options={'ordering': ('-sr', '-date')},
        ),
        migrations.AddField(
            model_name='querysrrecords',
            name='date',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]

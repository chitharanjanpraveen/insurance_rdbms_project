# Generated by Django 2.0.4 on 2018-04-16 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20180413_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominee',
            name='age',
            field=models.IntegerField(default=42),
            preserve_default=False,
        ),
    ]

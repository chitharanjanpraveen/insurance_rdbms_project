# Generated by Django 2.0.4 on 2018-04-10 21:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20180410_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='pass_word',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]

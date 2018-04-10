# Generated by Django 2.0.4 on 2018-04-10 16:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='office',
            fields=[
                ('office_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('adress', models.CharField(max_length=120)),
                ('phone_no', models.IntegerField()),
                ('manager_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='agent_office_name',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='agent.office'),
            preserve_default=False,
        ),
    ]
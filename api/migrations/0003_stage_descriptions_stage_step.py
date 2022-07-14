# Generated by Django 4.0.4 on 2022-07-12 05:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_stage_descriptions_remove_stage_steps'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='descriptions',
            field=models.JSONField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stage',
            name='step',
            field=models.JSONField(default={'steps': ['Step1', 'Step2']}),
            preserve_default=False,
        ),
    ]

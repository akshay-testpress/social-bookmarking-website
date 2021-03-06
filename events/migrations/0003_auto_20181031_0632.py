# Generated by Django 2.1.2 on 2018-10-31 06:32

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20181031_0600'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={},
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='event',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='event',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]

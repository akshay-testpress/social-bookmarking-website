# Generated by Django 2.0.8 on 2018-10-22 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20181022_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviesdirectors',
            name='middel_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
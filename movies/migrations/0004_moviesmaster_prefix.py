# Generated by Django 2.0.8 on 2018-10-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20181022_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesmaster',
            name='prefix',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
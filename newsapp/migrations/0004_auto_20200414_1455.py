# Generated by Django 3.0.5 on 2020-04-14 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_auto_20200414_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscatwise',
            name='author',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]
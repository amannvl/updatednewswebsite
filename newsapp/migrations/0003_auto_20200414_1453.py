# Generated by Django 3.0.5 on 2020-04-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_auto_20200414_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newscatwise',
            name='content',
            field=models.CharField(default='', max_length=280, null=True),
        ),
    ]
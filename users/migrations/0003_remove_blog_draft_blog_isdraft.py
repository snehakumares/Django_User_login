# Generated by Django 4.1.1 on 2022-10-08 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='draft',
        ),
        migrations.AddField(
            model_name='blog',
            name='isdraft',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

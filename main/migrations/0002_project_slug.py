# Generated by Django 2.0.5 on 2018-05-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]

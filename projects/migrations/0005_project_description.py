# Generated by Django 3.0.2 on 2020-01-31 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200131_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

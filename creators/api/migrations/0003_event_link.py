# Generated by Django 4.0.6 on 2022-07-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
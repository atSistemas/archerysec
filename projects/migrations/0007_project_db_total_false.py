# Generated by Django 3.1.2 on 2020-10-08 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20201008_0136'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_db',
            name='total_false',
            field=models.TextField(null=True),
        ),
    ]

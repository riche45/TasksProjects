# Generated by Django 4.2.1 on 2023-05-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_task_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project_key',
            field=models.IntegerField(default=False),
        ),
    ]

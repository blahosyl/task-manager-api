# Generated by Django 3.2.4 on 2024-07-28 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='excerpt',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]

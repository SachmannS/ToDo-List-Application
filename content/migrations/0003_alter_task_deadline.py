# Generated by Django 4.1.3 on 2024-03-27 10:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("content", "0002_alter_task_iscompleted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="deadLine",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
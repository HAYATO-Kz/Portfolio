# Generated by Django 3.1.5 on 2021-01-30 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210130_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(choices=[('1', 'Programming Language'), ('2', 'Frontend'), ('3', 'Backend'), ('4', 'Database'), ('5', 'Tool'), ('6', 'Other')], max_length=1),
        ),
    ]

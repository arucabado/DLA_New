# Generated by Django 4.2.7 on 2023-11-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_miembro_horai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='gametag',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='pais',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='zonah',
            field=models.CharField(default=None, max_length=30),
        ),
    ]

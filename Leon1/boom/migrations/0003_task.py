# Generated by Django 4.0.5 on 2022-07-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boom', '0002_weman'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
            ],
        ),
    ]

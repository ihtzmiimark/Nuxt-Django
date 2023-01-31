# Generated by Django 4.1.5 on 2023-01-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]

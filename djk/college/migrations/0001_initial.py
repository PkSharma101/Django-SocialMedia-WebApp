# Generated by Django 3.0.3 on 2020-04-11 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('msg', models.TextField()),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

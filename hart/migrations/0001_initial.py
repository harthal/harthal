# Generated by Django 3.0.3 on 2020-05-12 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hartal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=264)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField()),
            ],
        ),
    ]

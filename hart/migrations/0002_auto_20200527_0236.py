# Generated by Django 3.0.3 on 2020-05-27 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hartal',
            name='date',
        ),
        migrations.AddField(
            model_name='hartal',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hartal',
            name='type',
            field=models.CharField(default='', max_length=264),
        ),
        migrations.AlterField(
            model_name='hartal',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

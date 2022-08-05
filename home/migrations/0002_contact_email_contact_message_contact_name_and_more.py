# Generated by Django 4.1 on 2022-08-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=13),
        ),
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
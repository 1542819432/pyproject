# Generated by Django 3.0.3 on 2020-02-25 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200224_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='explain',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='matures',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='size',
        ),
    ]
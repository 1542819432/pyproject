# Generated by Django 3.0.3 on 2020-03-02 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='部门名')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='职工')),
                ('salary', models.FloatField(verbose_name='工资')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='department.Section', verbose_name='部门')),
            ],
        ),
    ]

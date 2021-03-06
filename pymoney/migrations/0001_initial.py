# Generated by Django 3.1.3 on 2020-11-17 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('budget', models.IntegerField()),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymoney.budget')),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymoney.budget')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymoney.category')),
            ],
        ),
    ]

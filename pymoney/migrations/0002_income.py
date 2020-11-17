# Generated by Django 3.1.3 on 2020-11-17 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pymoney', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymoney.budget')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pymoney.category')),
            ],
        ),
    ]

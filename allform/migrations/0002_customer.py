# Generated by Django 3.0.7 on 2021-07-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allform', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]

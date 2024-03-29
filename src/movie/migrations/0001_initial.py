# Generated by Django 3.2.6 on 2021-08-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='movie')),
                ('category', models.CharField(choices=[('A', 'ACTION'), ('D', 'DRAMA'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=1)),
                ('language', models.CharField(choices=[('EN', 'ENGLISH'), ('TR', 'TURKISH')], max_length=2)),
                ('status', models.CharField(choices=[('RA', 'RECEANTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2)),
                ('year_of_production', models.DateField()),
                ('view_count', models.IntegerField(default=0)),
            ],
        ),
    ]

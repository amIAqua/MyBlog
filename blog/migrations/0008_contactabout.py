# Generated by Django 2.2.5 on 2019-10-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191009_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=50)),
                ('city_of_living', models.CharField(max_length=30)),
                ('country_of_living', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.2.10 on 2024-11-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdId', models.CharField(max_length=100)),
                ('stdName', models.CharField(max_length=100)),
                ('stdCourse', models.CharField(max_length=100)),
                ('stdYear', models.CharField(max_length=100)),
            ],
        ),
    ]

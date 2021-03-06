# Generated by Django 3.0 on 2019-12-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=255)),
                ('blog_title', models.CharField(max_length=255)),
                ('blog_content', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Mentee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=255)),
                ('mentee_name', models.CharField(max_length=255)),
                ('mentee_testi', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=255)),
                ('mentor_name', models.CharField(max_length=255)),
                ('mentor_exp', models.CharField(max_length=255)),
                ('mentor_testi', models.CharField(max_length=255)),
            ],
        ),
    ]

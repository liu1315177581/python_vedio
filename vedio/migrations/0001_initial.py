# Generated by Django 2.1.1 on 2018-09-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_birth', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_birth', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('release_date', models.DateTimeField()),
                ('language_type', models.CharField(max_length=255, null=True)),
                ('url', models.CharField(max_length=255)),
                ('text_content', models.TextField(null=True)),
                ('place_origin', models.CharField(max_length=255, null=True)),
                ('row_url', models.CharField(max_length=255, null=True)),
                ('column_url', models.CharField(max_length=255, null=True)),
                ('actor_name', models.ManyToManyField(to='vedio.Actor')),
                ('director_name', models.ManyToManyField(to='vedio.Director')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='resources',
            name='tag',
            field=models.ManyToManyField(to='vedio.Tag'),
        ),
        migrations.AddField(
            model_name='resources',
            name='type',
            field=models.ManyToManyField(to='vedio.Type'),
        ),
        migrations.AddField(
            model_name='director',
            name='directors_work_name',
            field=models.ManyToManyField(to='vedio.Resources'),
        ),
        migrations.AddField(
            model_name='actor',
            name='actor_work_name',
            field=models.ManyToManyField(to='vedio.Resources'),
        ),
    ]

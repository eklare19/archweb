# Generated by Django 2.2.8 on 2019-12-18 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('website_rss', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'feeds',
                'db_table': 'feeds',
                'ordering': ('-title',),
                'get_latest_by': 'title',
            },
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Worldwide Planets',
                'db_table': 'planets',
                'ordering': ('-name',),
                'get_latest_by': 'name',
            },
        ),
        migrations.CreateModel(
            name='FeedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.CharField(max_length=2048)),
                ('author', models.CharField(max_length=255)),
                ('publishdate', models.DateTimeField(db_index=True, verbose_name='publish date')),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('feed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feed', to='planet.Feed')),
            ],
            options={
                'verbose_name_plural': 'Feed Items',
                'db_table': 'feeditems',
                'ordering': ('-publishdate',),
                'get_latest_by': 'publishdate',
            },
        ),
    ]

# Generated by Django 3.1 on 2022-01-10 16:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=39)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('brief_description', models.TextField()),
                ('content', models.TextField()),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(blank=True)),
                ('thumbnail', models.ImageField(upload_to='', verbose_name='thumbnails')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.category')),
                ('tags', models.ManyToManyField(to='blogs.Tags')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.post')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=69, null=True)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 1, 10, 22, 5, 57, 996956))),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(to='blogs.Tags'),
        ),
    ]
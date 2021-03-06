# Generated by Django 3.0.6 on 2020-06-04 09:52

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
            name='Job',
            fields=[
                ('job_id', models.IntegerField(primary_key=True, serialize=False)),
                ('job_title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=3000)),
                ('salary', models.IntegerField(max_length=255)),
                ('location', models.CharField(max_length=100)),
                ('contact_phone', models.IntegerField(max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

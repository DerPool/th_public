# Generated by Django 2.0.2 on 2018-04-18 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teamapp', '0002_auto_20180418_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='otklik',
            name='target_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

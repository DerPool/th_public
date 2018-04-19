# Generated by Django 2.0.2 on 2018-04-18 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(choices=[('3', 'Критично'), ('2', 'Важно'), ('1', 'Желательно')], max_length=10)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_desc', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('dateofcreation', models.DateTimeField()),
                ('status', models.CharField(choices=[('O', 'Открыта'), ('M', 'Модерация'), ('C', 'Закрыта')], max_length=1)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='tagassign',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teamapp.Vacancy'),
        ),
    ]

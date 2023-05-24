# Generated by Django 4.2.1 on 2023-05-24 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.test'),
        ),
        migrations.AlterField(
            model_name='taskoption',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='options', to='tests.task'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.test'),
        ),
        migrations.AlterField(
            model_name='usertest',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
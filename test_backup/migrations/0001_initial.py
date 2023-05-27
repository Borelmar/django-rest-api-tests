# Generated by Django 4.2.1 on 2023-05-25 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('options_count', models.PositiveIntegerField(default=0)),
                ('correct_answer_num', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TaskOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('ordinal_num', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(choices=[('russian_language', 'русский язык'), ('information_analysis', 'анализ информации'), ('computer_literacy', 'компьютерная грамотность')], max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('tasks_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=128)),
                ('correct_count', models.PositiveIntegerField(default=0)),
                ('incorrect_count', models.PositiveIntegerField(default=0)),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tests.test')),
            ],
        ),
    ]
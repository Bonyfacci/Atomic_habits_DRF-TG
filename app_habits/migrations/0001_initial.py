# Generated by Django 4.2.7 on 2023-11-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=100, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.TextField(verbose_name='Действие')),
                ('periodicity', models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения')),
                ('time_to_complete', models.IntegerField(verbose_name='Время на выполнение, в секундах')),
                ('pleasant_habit', models.BooleanField(default=False, verbose_name='Признак приятной привычки')),
                ('reward', models.TextField(blank=True, null=True, verbose_name='Вознаграждение за выполнение действия')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности привычки')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
                'ordering': ('pk',),
            },
        ),
    ]

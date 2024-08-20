# Generated by Django 5.0.7 on 2024-07-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.PositiveSmallIntegerField()),
                ('country', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('teacher_salary', models.PositiveSmallIntegerField(default=0)),
                ('hire_date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]

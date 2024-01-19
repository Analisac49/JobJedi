# Generated by Django 5.0.1 on 2024-01-19 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jedi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='user',
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='job_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='company',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='position',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 4.0.3 on 2022-03-15 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('time_posted', models.DateTimeField()),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirements.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='login.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Queries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('document_id', models.CharField(max_length=50)),
                ('status_check', models.BooleanField(default=False)),
                ('time_posted', models.DateTimeField()),
                ('requirement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requirements.requirement')),
            ],
        ),
    ]

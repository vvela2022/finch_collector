# Generated by Django 4.1.1 on 2022-10-03 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discoverer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('length', models.IntegerField(default=0)),
                ('Birds', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discoverer', to='main_app.birds')),
            ],
        ),
    ]

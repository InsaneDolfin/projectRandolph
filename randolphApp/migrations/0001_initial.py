# Generated by Django 2.0.7 on 2018-07-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Jeux',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('section', models.CharField(max_length=50)),
                ('note', models.CharField(max_length=500)),
                ('disponibilite', models.CharField(max_length=50)),
                ('etage', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='genre',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='randolphApp.Jeux'),
        ),
    ]

# Generated by Django 3.0.7 on 2020-10-19 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('sinopsis', models.TextField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('año', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieCalification.Pelicula')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Usuario')),
            ],
        ),
    ]

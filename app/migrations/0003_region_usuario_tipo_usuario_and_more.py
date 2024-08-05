# Generated by Django 4.2 on 2024-05-24 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_propiedad_usuario_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.CharField(choices=[('arrendatario', 'Arrendatario'), ('arrendador', 'Arrendador')], default='arrendatario', max_length=15),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='comuna_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.comuna'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='tipo_propiedad_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.tipo_propiedad'),
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.region')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='provincia_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='app.provincia'),
        ),
    ]
# Generated by Django 4.1.6 on 2023-07-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_pays_dmi_dmi_pays_dmi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_fichier', models.CharField(max_length=250)),
                ('nature_fichier', models.CharField(max_length=250)),
                ('type_pi', models.CharField(max_length=250)),
                ('date_ajout', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
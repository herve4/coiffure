# Generated by Django 4.2.2 on 2023-09-23 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coiffuresapp', '0008_alter_client_montant_alter_client_telephone_cl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='montant',
            field=models.CharField(default=0, max_length=6, verbose_name='Montant'),
        ),
    ]

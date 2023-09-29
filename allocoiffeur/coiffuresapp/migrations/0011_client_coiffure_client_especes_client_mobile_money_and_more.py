# Generated by Django 4.2.2 on 2023-09-23 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coiffuresapp', '0010_alter_client_adresse_cl'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='coiffure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coiffuresapp.coiffuresgaleries', verbose_name='Coiffure'),
        ),
        migrations.AddField(
            model_name='client',
            name='especes',
            field=models.BooleanField(blank=True, null=True, verbose_name='Espèces'),
        ),
        migrations.AddField(
            model_name='client',
            name='mobile_money',
            field=models.BooleanField(blank=True, null=True, verbose_name='Mobile Money'),
        ),
        migrations.AddField(
            model_name='client',
            name='payer',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='paypal',
            field=models.BooleanField(blank=True, null=True, verbose_name='Paypal'),
        ),
        migrations.AddField(
            model_name='client',
            name='stripe',
            field=models.BooleanField(blank=True, null=True, verbose_name='Stripe'),
        ),
        migrations.DeleteModel(
            name='payment',
        ),
    ]
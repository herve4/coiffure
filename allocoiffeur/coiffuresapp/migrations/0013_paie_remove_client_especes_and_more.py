# Generated by Django 4.2.2 on 2023-09-24 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coiffuresapp', '0012_alter_client_especes_alter_client_mobile_money_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='paie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_money', models.CharField(blank=True, max_length=15, null=True, verbose_name='Mobile Money')),
                ('stripe', models.CharField(blank=True, max_length=15, null=True, verbose_name='Stripe')),
                ('paypal', models.CharField(blank=True, max_length=15, null=True, verbose_name='Paypal')),
                ('especes', models.CharField(blank=True, max_length=15, null=True, verbose_name='Espèces')),
            ],
            options={
                'verbose_name': 'Paie',
                'verbose_name_plural': 'Paies',
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='especes',
        ),
        migrations.RemoveField(
            model_name='client',
            name='mobile_money',
        ),
        migrations.RemoveField(
            model_name='client',
            name='paypal',
        ),
        migrations.RemoveField(
            model_name='client',
            name='stripe',
        ),
        migrations.AddField(
            model_name='coiffuresgaleries',
            name='paie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coiffuresapp.paie', verbose_name='Paiement'),
        ),
    ]

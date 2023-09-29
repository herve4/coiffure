# Generated by Django 4.2.2 on 2023-09-24 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coiffuresapp', '0014_client_paie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paie',
            name='especes',
        ),
        migrations.RemoveField(
            model_name='paie',
            name='mobile_money',
        ),
        migrations.RemoveField(
            model_name='paie',
            name='paypal',
        ),
        migrations.RemoveField(
            model_name='paie',
            name='stripe',
        ),
        migrations.AddField(
            model_name='paie',
            name='type',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Type'),
        ),
    ]
# Generated by Django 4.2.2 on 2023-09-25 09:08

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('coiffuresapp', '0016_remove_coiffuresgaleries_paie_alter_client_paie'),
    ]

    operations = [
        migrations.CreateModel(
            name='typeCoiffure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='Coiffure pour')),
            ],
            options={
                'verbose_name': 'Coiffure pour',
                'verbose_name_plural': 'Coiffures pour',
            },
        ),
        migrations.AddField(
            model_name='categoriscoiffures',
            name='img_couverture',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[350, 350], upload_to='media/catégories'),
        ),
        migrations.AddField(
            model_name='coiffuresgaleries',
            name='coiffurePour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coiffuresapp.typecoiffure', verbose_name='Coiffure pour'),
        ),
    ]

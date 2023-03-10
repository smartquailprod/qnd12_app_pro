# Generated by Django 3.2.13 on 2022-09-09 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('webapp_v10', '0015_remove_galeriadeimagenes_5_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='galeriadeimagenes_5',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen Isla Florena'),
        ),
        migrations.AddField(
            model_name='galeriadeimagenes_5',
            name='logo_0',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Imagen Isla Florena'),
        ),
    ]

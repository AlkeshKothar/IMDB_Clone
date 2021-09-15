# Generated by Django 3.2.6 on 2021-09-15 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_app', '0003_auto_20210915_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist', to='imdb_app.streamplatfrom'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-10 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodreviews', '0015_auto_20190310_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodreviews.Review'),
        ),
    ]
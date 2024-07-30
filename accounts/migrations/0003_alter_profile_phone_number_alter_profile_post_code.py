# Generated by Django 5.0.7 on 2024-07-30 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, choices=[('+998', 'Uz'), ('+7', 'Ru')], default='+998', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='post_code',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
    ]

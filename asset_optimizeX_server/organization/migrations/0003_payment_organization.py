# Generated by Django 4.2.6 on 2023-10-21 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organization_premiumuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization'),
        ),
    ]

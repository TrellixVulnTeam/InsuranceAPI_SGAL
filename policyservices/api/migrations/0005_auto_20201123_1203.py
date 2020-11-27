# Generated by Django 3.1.3 on 2020-11-23 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201123_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='bodilyInjuryLiability',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='collision',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='comprehensive',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AlterField(
            model_name='policy',
            name='fuel',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='policy',
            name='personalInjuryProtection',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='propertyDamageLiability',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='purchaseDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='policy',
            name='vehicleSegment',
            field=models.CharField(max_length=1),
        ),
    ]

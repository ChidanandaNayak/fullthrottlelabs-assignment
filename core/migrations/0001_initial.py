# Generated by Django 2.1 on 2020-06-06 14:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('real_name', models.CharField(max_length=100)),
                ('tz', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='activityperiods',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_period', to='core.Member'),
        ),
    ]
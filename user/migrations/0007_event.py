# Generated by Django 2.1 on 2018-09-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180927_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('king', models.IntegerField(null=True)),
                ('modality', models.CharField(blank=True, choices=[('fr', 'Free'), ('pd', 'Paid')], max_length=2, null=True)),
                ('forbidden', models.BooleanField(default=False)),
                ('drinks', models.BooleanField(default=False)),
                ('type', models.CharField(blank=True, choices=[('p', 'Rolê Pequeno'), ('m', 'Rolê Médio'), ('g', 'Moster grande porte')], max_length=2, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('capacity', models.IntegerField(default=10)),
                ('image', models.ImageField(default='event_logo/default.jpg', upload_to='event_logo/')),
            ],
        ),
    ]
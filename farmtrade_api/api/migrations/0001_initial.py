# Generated by Django 5.0 on 2023-12-22 09:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photos/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_photos/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='product_photos/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(choices=[('Aceh', 'Aceh'), ('Bali', 'Bali'), ('Bangka Belitung', 'Bangka Belitung'), ('Banten', 'Banten'), ('Bengkulu', 'Bengkulu'), ('Gorontalo', 'Gorontalo'), ('DKI Jakarta', 'DKI Jakarta'), ('Jambi', 'Jambi'), ('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('Jawa Timur', 'Jawa Timur'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Lampung', 'Lampung'), ('Maluku', 'Maluku'), ('Maluku Utara', 'Maluku Utara'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Papua', 'Papua'), ('Papua Barat', 'Papua Barat'), ('Riau', 'Riau'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Tenggara', 'Sulawesi Tenggara'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Sumatera Barat', 'Sumatera Barat'), ('Sumatera Selatan', 'Sumatera Selatan'), ('Sumatera Utara', 'Sumatera Utara'), ('Yogyakarta', 'Yogyakarta')], max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userprofile')),
            ],
            options={
                'ordering': ('-date_added',),
            },
        ),
    ]

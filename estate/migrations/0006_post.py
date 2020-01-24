# Generated by Django 3.0.2 on 2020-01-23 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('estate', '0005_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_image', models.ImageField(upload_to='posts/')),
                ('description', models.TextField(max_length=300)),
                ('location', models.CharField(max_length=100)),
                ('bedrooms_no', models.PositiveIntegerField()),
                ('bathrooms_no', models.PositiveIntegerField()),
                ('phone_no', models.PositiveIntegerField()),
                ('cost', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 3.2.6 on 2022-04-26 17:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_pandit_imageurl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('reviewText', models.TextField(verbose_name='Reviews Text')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('yourRating', models.IntegerField(default=0, validators=[main.models.minMax3])),
                ('pujaName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.puja')),
            ],
        ),
    ]

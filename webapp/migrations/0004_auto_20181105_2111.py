# Generated by Django 2.0.3 on 2018-11-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_in_school', models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]

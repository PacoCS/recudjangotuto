# Generated by Django 2.2.5 on 2019-09-30 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Answer',
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('vote_date', models.DateTimeField(verbose_name='date voted')),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Answer')),
            ],
        ),
    ]

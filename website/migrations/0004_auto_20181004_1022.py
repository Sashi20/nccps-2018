# Generated by Django 2.1 on 2018-10-04 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20180919_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validate_ans', models.BooleanField()),
                ('attempted', models.BooleanField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_1', models.CharField(max_length=255)),
                ('option_2', models.CharField(max_length=255)),
                ('option_3', models.CharField(max_length=255)),
                ('option_4', models.CharField(max_length=255)),
                ('correct_answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='answerpaper',
            name='answered_q',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Question'),
        ),
        migrations.AddField(
            model_name='answerpaper',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Profile'),
        ),
    ]

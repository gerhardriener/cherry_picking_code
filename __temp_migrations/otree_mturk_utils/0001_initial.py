# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-08 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import radiogrid.db


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BigFiveData',
            fields=[
                ('Participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='asdf', serialize=False, to='otree.Participant')),
                ('bigfive', radiogrid.db.RadioGridField(require_all_fields=True, rows=((1, 'Extraverted, enthusiastic'), (2, 'Critical, quarrelsome'), (3, 'Dependable, self-disciplined'), (4, 'Anxious, easily upset'), (5, 'Open to new experiences, complex'), (6, 'Reserved, quiet'), (7, 'Sympathetic, warm'), (8, 'Disorganized, careless'), (9, 'Calm, emotionally stable'), (10, 'Conventional, uncreative'), (11, 'Otree Hackathon, hacking')), values=((1, 'Disagree strongly'), (2, 'Disagree moderately'), (3, 'Disagree a little'), (4, 'Neither agree nor Disagree'), (5, 'Agree a little'), (6, 'Agree moderately'), (7, 'Agree strongly')), verbose_name='I see myself as')),
            ],
        ),
        migrations.CreateModel(
            name='Mturk',
            fields=[
                ('Participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='otree.Participant')),
                ('current_wp', otree.db.models.IntegerField(null=True)),
                ('outofthegame', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='WPJobRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', otree.db.models.StringField(max_length=10000, null=True)),
                ('page_index', otree.db.models.IntegerField(null=True)),
                ('last_correct_answer', otree.db.models.IntegerField(null=True)),
                ('tasks_attempted', otree.db.models.PositiveIntegerField(default=0, null=True)),
                ('tasks_correct', otree.db.models.PositiveIntegerField(default=0, null=True)),
                ('mturker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree_mturk_utils.Mturk')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WPTimeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', otree.db.models.StringField(max_length=10000, null=True)),
                ('page_index', otree.db.models.IntegerField(null=True)),
                ('startwp_timer_set', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('startwp_time', otree.db.models.PositiveIntegerField(null=True)),
                ('endwp_time', otree.db.models.PositiveIntegerField(null=True)),
                ('mturker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree_mturk_utils.Mturk')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

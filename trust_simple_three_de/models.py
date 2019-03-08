from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import itertools


doc = """
Three person trust game with binary decisions
"""


class Constants(BaseConstants):
    name_in_url = 'team_work'
    players_per_group = 3
    num_rounds = 1

    instructions_template = 'trust_simple_three/Instructions.html'
    instructions_decision = 'trust_simple_three/InstrucDecisionSituation.html'


class Subsession(BaseSubsession):
    def creating_session(self):
        treatments = itertools.cycle([1, 2, 3])
        for g in self.get_groups():
            g.treatment = next(treatments)


class Group(BaseGroup):
    treatment = models.IntegerField()
    sent_amount = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        doc="""Decision by P1""",
    )

    sent_back_amount_1 = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        doc="""Decision by P2""",
    )
    sent_back_amount_2 = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        doc="""Decision by P3""",
    )

    sent_back_amount_2_direct_hypo = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        doc="""Hypothetical decision by P3""",
    )

    sent_back_amount_2_if_A = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        doc="""Decision by P3""",
    )

    sent_back_amount_2_if_B = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        doc="""Decision by P3""",
    )



class Player(BasePlayer):
    pass

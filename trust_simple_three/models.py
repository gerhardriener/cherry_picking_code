from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c
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
        widget=widgets.RadioSelect,
        doc="""Decision by P1""",
    )

    sent_back_amount_1 = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        widget=widgets.RadioSelect,
        doc="""Decision by P2""",
    )
    sent_back_amount_2 = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        widget=widgets.RadioSelect,
        doc="""Decision by P3""",
    )

    sent_back_amount_2_direct_hypo = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        widget=widgets.RadioSelect,
        doc="""Hypothetical decision by P3""",
    )

    sent_back_amount_2_if_A = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        widget=widgets.RadioSelect,
        doc="""Decision by P3""",
    )

    sent_back_amount_2_if_B = models.IntegerField(
        choices=[
            [0, 'Option L'],
            [1, 'Option R'],
        ],
        widget=widgets.RadioSelect,
        doc="""Decision by P3""",
    )


class Player(BasePlayer):
    prolific_id_get = models.StringField()
    prolific_id = models.StringField()
    CQ_maxA = models.IntegerField(
        choices=[
            [6,  '6 ECU'],
            [12, '12 ECU'],
            [10, '10 ECU'],
            [0,  '0 ECU'],
            [14, '14 ECU']
        ],
        widget=widgets.RadioSelect,
        doc="""Control question: Maximum amount a can earn""",
    )
    CQ_payoff = models.IntegerField(
        choices=[
            [6,  '6 ECU'],
            [12, '12 ECU'],
            [10, '10 ECU'],
            [0,  '0 ECU'],
            [14, '14 ECU']
        ],
        widget=widgets.RadioSelect,
        doc="""Control question: Payoff of B1""",
    )

    CQ_sumtask = models.IntegerField(
        doc="""Control question: Payoff of B1""",
    )

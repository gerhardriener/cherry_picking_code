from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Introduction(Page):
    timeout_seconds = 600
    def vars_for_template(self):
        return {'treatment': self.group.treatment}

class Send(Page):

    form_model = 'group'
    form_fields = ['sent_amount']
    def vars_for_template(self):
        return {'treatment': self.group.treatment}

    def is_displayed(self):
        return self.player.id_in_group == 1

class WaitForP1(WaitPage):
    pass

class SendBack1(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount_1']
    def vars_for_template(self):
        return {'treatment': self.group.treatment}

    def is_displayed(self):
        return self.player.id_in_group == 2


class WaitForP2(WaitPage):
    pass


class SendBack2(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount_2']
    def vars_for_template(self):
        return {'treatment': self.group.treatment}

    def is_displayed(self):
        return (self.player.id_in_group == 3 and self.group.treatment == 1)

class SendBack2Direct(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount_2']


    def is_displayed(self):
        return (self.player.id_in_group == 3 and self.group.treatment == 2)

    def vars_for_template(self):
        return {
            'sent_back_amount_1': self.group.sent_back_amount_1,
            'treatment': self.group.treatment
        }

class SendBack2DirectHypo(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount_2_direct_hypo']

    def is_displayed(self):
        return (self.player.id_in_group == 3 and self.group.treatment == 2)

    def vars_for_template(self):
        return {
            'sent_back_amount_1': self.group.sent_back_amount_1,
            'treatment': self.group.treatment
        }


class SendBack2Strategy(Page):

    form_model = 'group'
    form_fields = ['sent_back_amount_2_if_A',
                   'sent_back_amount_2_if_B']

    def is_displayed(self):
        return (self.player.id_in_group == 3 and self.group.treatment == 3)

    def vars_for_template(self):
        return {'treatment': self.group.treatment}

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        group = self.group
        p1 = group.get_player_by_id(1)
        p2 = group.get_player_by_id(2)
        p3 = group.get_player_by_id(3)

        if group.treatment == 3 and group.sent_back_amount_1 == 0:
            group.sent_back_amount_2 = group.sent_back_amount_2_if_A
        elif group.treatment == 3 and group.sent_back_amount_1 == 1:
            group_sent_back_amount_2 = group.sent_back_amount_2_if_B
        # else:
        #    group.sent_back_amount_2 = group.sent_back_amount_2

        p1.payoff = (1 - group.sent_amount) * 5 + group.sent_amount * (group.sent_back_amount_1 * 6  + group.sent_back_amount_2 * 6)
        p2.payoff = (1 - group.sent_amount) * 5 + group.sent_amount * (group.sent_back_amount_1 * 10 + (1 - group.sent_back_amount_1 ) * 14)
        p3.payoff = (1 - group.sent_amount) * 5 + group.sent_amount * (group.sent_back_amount_2 * 10 + (1 - group.sent_back_amount_2 ) * 14)


class Results(Page):
    pass


page_sequence = [
    Introduction,
    Send,
    WaitForP1,
    SendBack1,
    WaitForP2,
    SendBack2,
    SendBack2Direct,
    SendBack2DirectHypo,
    SendBack2Strategy,
    ResultsWaitPage,
    Results,
]

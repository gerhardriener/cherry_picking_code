from otree.api import Currency as c, currency_range, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):
    cases = [
        {'offer': 1,  'return_1': 1, 'return_2': 1, 'return_2_A': 1, 'return_2_B': 1, 'p1_payoff': 5, 'p2_payoff': 5, 'p3_payoff': 5},
    ]

    def play_round(self):
        case = self.case
        if self.player.id_in_group == 1:
            yield (pages.Send, {"sent_amount": case['offer']})

        else:
            for invalid_return in [-1, case['offer'] * Constants.multiplier + 1]:
                yield SubmissionMustFail(pages.SendBack,
                                         {'sent_back_amount_1': invalid_return})
            yield (pages.SendBack, {'sent_back_amount_1': case['return']})

        if self.player.id_in_group == 1:
            expected_payoff = case['p1_payoff']
        else:
            expected_payoff = case['p2_payoff']

        assert self.player.payoff == expected_payoff

import random

from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import load_solution_function


class Adventure(BaseAdventure):

    title = _('Alternation')
    choices = ['red', 'green', 'blue']

    def test(self, file):
        function = load_solution_function(file)
        correct_argument = random.choice(self.choices)
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = (random.choice(self.choices)
                          + random.choice(self.choices))
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))

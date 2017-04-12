import random

from story.adventures import AdventureVerificationError, BaseAdventure

from ..data import _
from ..utils import get_random_string, load_solution_function


class Adventure(BaseAdventure):

    title = _('Negated character classes')
    dictionary = 'abcdefghijlmnopqrstuvwxyz'

    def test(self, file):
        function = load_solution_function(file)
        correct_argument = get_random_string(self.dictionary, 1, 5)
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = '{}{}'.format(
            random.randint(0, 9),
            get_random_string(self.dictionary, 1, 5)
        )
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))

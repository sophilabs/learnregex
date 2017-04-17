import random

from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import load_solution_function


class Adventure(BaseAdventure):

    title = _('Groups')

    def test(self, file):
        function = load_solution_function(file)
        correct_argument = 'hello' * random.randint(1, 5) + random.choice(
            ['python', 'pyschool']
        )
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = random.choice(['python', 'pyschool'])
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))

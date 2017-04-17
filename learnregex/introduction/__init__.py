from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import load_solution_function


class Adventure(BaseAdventure):

    title = _('Introduction')

    def test(self, file):
        function = load_solution_function(file)
        correct_argument = 'Python'
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = 'ython'
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))

import string

from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import get_random_string, load_solution_function


class Adventure(BaseAdventure):

    title = _('The dot')
    dictionary = string.ascii_lowercase + string.digits + string.punctuation

    def test(self, file):
        function = load_solution_function(file)
        correct_argument = 'python{}python'.format(
            get_random_string(self.dictionary, 1, 1)
        )
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = 'pythonpython'
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))

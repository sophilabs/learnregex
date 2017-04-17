import string

from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import get_random_string, load_solution_function


class Adventure(BaseAdventure):

    title = _('Capturing')
    dictionary = string.ascii_lowercase + string.digits

    def test(self, file):
        function = load_solution_function(file)
        repeat = get_random_string(self.dictionary, 4, 6)
        correct_argument = '{0}|{0}'.format(repeat)
        if not function(correct_argument):
            raise AdventureVerificationError(
                _("Your function didn't return True when executed with a "
                  "correct argument '{}'.".format(correct_argument))
            )
        wrong_argument = '{}|{}'.format(
            get_random_string(self.dictionary, 5, 5),
            get_random_string(self.dictionary, 5, 5)
        )
        if function(wrong_argument):
            raise AdventureVerificationError(
                _("Your function returned True when executed with a wrong "
                  "argument '{}'.".format(wrong_argument)))

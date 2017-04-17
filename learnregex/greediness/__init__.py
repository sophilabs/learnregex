import string

from story.adventures import AdventureVerificationError, BaseAdventure
from story.translation import gettext as _

from ..utils import get_random_string, load_solution_function


class Adventure(BaseAdventure):

    title = _('Greediness')
    dictionary = string.ascii_lowercase + string.digits

    def test(self, file):
        function = load_solution_function(file)
        prefix = get_random_string(self.dictionary, 1, 5) + ','
        correct_argument = '{}{},{}'.format(
            prefix,
            get_random_string(self.dictionary, 1, 5),
            get_random_string(self.dictionary, 1, 5),
        )
        result = function(correct_argument)
        if result != prefix:
            raise AdventureVerificationError(
                _("Your function didn't return the expected string '{}' when "
                  "executed with '{}'. "
                  "It returned '{}'.".format(prefix, correct_argument, result))
            )

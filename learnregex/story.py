from story.story import BaseStory
from story.translation import gettext as _

from . import (alternation, anchors, capturing, character_classes, greediness,
               groups, introduction, negated_character_classes, quantifiers,
               special_characters, the_dot)


class Story(BaseStory):

    name = 'learnregex'
    title = _('Learn regular expressions with Python')
    adventures = [
        introduction,
        special_characters,
        character_classes,
        negated_character_classes,
        the_dot,
        quantifiers,
        greediness,
        anchors,
        alternation,
        groups,
        capturing,
    ]

from story.story import BaseStory

from . import (character_classes, introduction, negated_character_classes,
               quantifiers, special_characters, the_dot)
from .data import _


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
    ]

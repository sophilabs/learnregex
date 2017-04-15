from story.story import BaseStory

from . import introduction
from .data import _


class Story(BaseStory):

    name = 'learnregex'
    title = _('Learn regular expressions with Python.')
    adventures = [
        introduction
    ]

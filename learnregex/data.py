import gettext
import os

domain = 'learnregex'
localedir = os.path.join(os.path.dirname(__file__), 'locale/')
gettext.bindtextdomain(domain, localedir)
translation = gettext.translation(domain, localedir, fallback=True)


def _(msg):
    return gettext.dgettext(domain, msg)

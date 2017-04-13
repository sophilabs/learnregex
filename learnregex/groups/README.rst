Groups

Groups have plenty of uses. They basically enclose a section of our
expression so we can treat it as a token. This allows us to apply quantifiers
to a whole expression instead of a single character or character class like
we have been doing. It also allows us to use the alternation operator with a
limited scope.

Groups are defined with simple parenthesis. We can put everything inside them,
even other groups.

For this adventure, write a python function that receives a string and
returns `True` if starts with one or more repetitions of the word 'hello' and
ends with either 'python' or 'pyschool', and `False` otherwise. You don't
need to check for spaces, the words just need to follow one immediately after
another.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

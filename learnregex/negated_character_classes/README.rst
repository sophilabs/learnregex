When the first character inside a character class is a caret (remember this
is a special character), it transforms our character class into a negated
character class, meaning it will match any character that's not in our set.

For this adventure, write a python function that receives a string and
returns `True` if the first character is not a number, and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

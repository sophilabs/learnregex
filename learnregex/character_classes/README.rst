Now that we now what are special characters and how to escape them, let's try
their actual special meaning. We are going to start with character classes.

A character class matches one out of a set of characters that we define. You
define a character class by writing all the characters of your set between
square brackets. For example, this matches either an "a" or a "b": [ba] (the
order doesn't matter).

For this adventure, write a python function that receives a string and
returns `True` if the first character is a digit, and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

Searching for literal strings is really simple and we wouldn't really need
regular expressions to do it. Where regular expressions really shine is in
matching patterns, and to do so it must define a set of characters with
special meaning.

The following characters are considered special and you must "escape" them if
you want to use them literally.

.. sourcecode:: bash

    . ? * + ^ $ ( ) [ ] {{ }} | \

The closing square bracket ] and closing curly brace }} can be used
literally without escaping them and their meaning will be determined by the
presence of their opening counterparts, but it's clearer to escape them every
time you want to use them literally.

To escape a special character you put a backslash (here the backslash is
using its special meaning!) before them.

For this adventure, write a python function that receives a string and
returns `True` if it contains a backslash, and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

HINT
____

The backslash is also a special character in Python's string literals. To
avoid issues, define your regular expressions as "raw strings".

Normal string: 'hello'
Raw string: r'hello'

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

Quantifiers

This is one of the most interesting features of regular expressions. It
allows us to match any number of repetitions of a character (or character
class, or sequence of characters). We have three predefined quantifiers that
cover the most common use cases plus a fourth generic one which is a bit
longer, but covers all possible cases.

?: match the preceding token zero or one time.
*: match the preceding token zero or more times.
+: match the preceding token one or more times.
{{min,max}}: match the preceding token n times such that min <= n <= max. You
can omit the max (but leaving the comma) to make it infinite. If you omit
both the comma and the max, it matches the preceding token exactly "min"
times.

For this adventure, write a python function that receives a string and
returns `True` if it starts with a digit, followed by zero or more spaces,
followed by another digit; and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

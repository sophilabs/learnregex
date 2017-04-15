Alternation

If you want to match different regular expressions on the same string, you
can use the alternation operator (the pipe symbol |) to separate different
expressions and instruct the engine to try to match either what's to the left
of it or, if it fails, what's to the right of it.

The alternation operator has the lowest precedence of all operators, meaning
that the engine will try to match everything to its left as a whole and
everything to its right (assuming the previous match failed) as a whole. If
you want to limit the scope of the operator to use it inside a tiny part of a
more complex expression you will need to learn how "groups" work. Luckily for
you, that's the next adventure.

For this adventure, write a python function that receives a string and
returns `True` if it's either 'red', 'green' or 'blue'; and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

HINT
----
You can use multiple alternation operators, they resolve from left to
right. That means that the expression 'aa|bb|cc' will try to match 'aa'
first, if it fails it will follow with 'bb|cc' where it will again split
the expressions between the alternation operator and start with 'bb', and
so on...

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

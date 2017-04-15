When using quantifiers sometimes we'll run into an issue where they match
more than we want. Suppose we want to match the first part (including the
dot) of a domain. We write the expression '.*\.' thinking "this will return
all the characters before the first dot along with it" and test it on
"pyschool.github.io" expecting to get "pyschool." back, but it returns
"pyschool.github.".

What happened? Quantifiers are greedy by default, meaning they will match
all the characters they can. In this case we have two dots in our string, so
the quantifier gets to match all the characters up to the last dot without
problem.

We can make our quantifiers "lazy" by adding a question mark at their end
(even the ? quantifier, which becomes ?? in its lazy form), meaning they will
match the minimum amount of characters they can. If we add a question mark to
our quantifier it becomes lazy and will now match all the characters up to
the first dot and stop there, since the whole expression matches.

For this adventure, write a python function that receives a string of comma
separated values and returns all the characters from the start up to the
first comma, including it.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

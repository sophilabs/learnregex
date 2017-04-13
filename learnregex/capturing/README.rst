Groups provide an additional feature: they capture the string they end up
matching and save it in a variable that we can use later, either in the same
regular expression or after it finishes. In python we can use a captured
group with a backslash and an index. For example: \1 will reference the first
group of our regular expression, \2 will reference the second and so on until
\9, where we run out of numbers (they can only use one digit). If you need to
capture more than 9 groups check out named groups.

Say we want to test if a string ends with the same character it started. We
could write something like this: '^(.).*\1$|^.$'. We capture the first
character after the start of the string, match zero o more characters in
between and reference the captured character before the string ends. We also
alternate with another expression in case our string has only 1 character.

For this adventure, write a python function that receives a string with only
one pipe ('|') somewhere in between and returns `True` if everything to the
left of the pipe equals what's to its right, and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

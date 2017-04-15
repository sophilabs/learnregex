Anchors allow us to match specific positions inside a string instead of a
character. They belong to a group called zero-length matches for this reason.

With anchors we can match the start and end of a string using ^ and $
respectively.

For this adventure, write a python function that receives a string and
returns `True` if it ends with a caret, and `False` otherwise.

You can use this template to get started:

.. sourcecode:: python

    import re

    def test(string):
        # Your code goes here

When you are done, you must run:

.. sourcecode:: bash

    $ {script} verify program.py

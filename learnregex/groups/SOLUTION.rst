`program.py` content:

.. sourcecode:: python

    import re


    def test(string):
        return re.match(r'(hello)+(python|pyschool)', string)


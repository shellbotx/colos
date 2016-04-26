import random
from colorschemes import NAMEHERE

class NAMEHERE(object):
    """ Docstring """

    def __init__(self):
        self.name = "NAMEHERE"
        self.source = "http://github.com/SOURCEHERE"

        self.foo()

    def foo(self):
        # Comment
        string = str("Hello World")
        number = int(012345.543210)
        boolean = True
        
        if random.randint(0, 10) < 5 or boolean:
            print ("something\nsomething\nsomething")

        return {string, number, boolean}

    @decoration
    def highlight(self, params=None):
        return params

# TODO Go to github.com/shellbotx/colos

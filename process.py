"""
Generate README.md and model python classes for each
colorscheme.
"""
import os

colorschemes = {
    'Badwolf':        { 'source': 'sjl/badwolf' },
    'Blackboard':     { 'source': 'nelstrom/vim-blackboard' },
    'Cobalt2':        { 'source': 'herrbischoff/cobalt2.vim' },
    'Dracula':        { 'source': 'zenorocha/dracula-theme' },
    'Gotham':         { 'source': 'whatyouhide/vim-gotham' },
    'Gruvbox':        { 'source': 'morhetz/gruvbox' },
    'Flatlandia':     { 'source': 'jordwalke/flatlandia' },
    'Molokai':        { 'source': 'tomasr/molokai' },
    'OceanicNext':    { 'source': 'mhartington/oceanic-next' },
    'Pyte':           { 'source': 'vim-scripts/pyte' },
    'Railscasts':     { 'source': 'jpo/vim-railscasts-theme' },
    'Solarized':      { 'source': 'altercation/vim-colors-solarized' },
    'Summerfruit256': { 'source': 'vim-scripts/summerfruit256.vim' }
}

readme = open('README.md', 'w')
readme.write('## COLOS\n')
readme.write('COLOS is a collection of high quality vim colorschemes.\n')

# Using iterator to allow for alphabetical sorting
iterator = iter(sorted(colorschemes.items()))
try:
    while True:
        colorscheme = next(iterator)
        name = colorscheme[0]
        source = colorscheme[1]['source']

        model = open('models\%s.py' % (name.lower()), 'w')

        model.write("\
import random \n\
from colorschemes import {1} \n\n\
class {0}(object): \n\
    \"\"\" Docstring \"\"\" \n\n\
    def __init__(self): \n\
        self.name = \'{1}\' \n\
        self.source = \"http://github.com/{2}\" \n\n\
        self.foo() \n\n\
    def foo(self): \n\
        # Comment \n\
        string = str(\"Hello World\") \n\
        number = int(012345.543210) \n\
        boolean = True \n\n\
        if random.randint(0, 10) < 5 or boolean: \n\
            print (\"something\\nsomething\\nsomething\") \n\n\
        return {{string, number, boolean}} \n\n\
    @decoration \n\
    def html(self, params=None): \n\
        return params\n\n\
#TODO Go to github.com/shellbotx/colos".format(name, name.lower(), source))
        model.close()

        readme.write("### [{0}](http://github.com/{2})\n![{1} screenshot](img/{1}.png)\n<hr>\n\n"\
                     .format(name, name.lower(), source))

except StopIteration:
    pass

finally:
    del iterator

readme.write('_Font: SourceCodePro 12 bold_')
readme.close()

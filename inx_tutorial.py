#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inkscape extension to introduce basic inx file communication
"""

import os
import inkex

class InxTutorial(inkex.Effect):
    def add_arguments(self, pars):
        pars.add_argument("--mystring", type=str, default="",
            help="This is help text for mystring")
        pars.add_argument("--mypath", default=os.path.expanduser("~"),
            help="This is help text for mypath")
        pars.add_argument("--mybool", type=inkex.Boolean, default=False,
            help="This is help text for mybool")
        pars.add_argument("--myint", type=int, default=0,
            help="This is help text for myint")
        pars.add_argument("--myfloat", type=float, default=0.0,
            help="This is help text for myfloat")
        pars.add_argument("--myoptiongroup", default="first selection",
            help="This is help text for myselection")

    def effect(self):
        inkex.errormsg(f'mybool: {self.options.mybool}')
        inkex.errormsg(f'mystring: {self.options.mystring}')
        inkex.errormsg(f'myint: {self.options.myint}')
        inkex.errormsg(f'myfloat: {self.options.myfloat}')
        inkex.errormsg(f'selected item: {self.options.myoptiongroup}')
        inkex.errormsg(f'ids of currently selected inkscape objects: {self.options.ids}')
        inkex.errormsg(f'list of currently selected inkscape objects: {self.svg.selected}')

if __name__ == '__main__':
    InxTutorial().run()

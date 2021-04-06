#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inkscape extension to introduce basic inx file communication
"""

import inkex

class InxTutorial(inkex.Effect):
	def __init__(self):
		inkex.Effect.__init__(self)
		self.arg_parser.add_argument(
			'-b', '--mybool',
			type=bool,
			dest='mybool',
			help='This is help text for mybool'
			)
		self.arg_parser.add_argument(
			'-s', '--mystring',
			type=str,
			dest='mystring',
			help='This is help text for mystring'
			)
		self.arg_parser.add_argument(
			'-i', '--myint',
			type=int,
			dest='myint',
			help='This is help text for myint'
			)
		self.arg_parser.add_argument(
			'-f', '--myfloat',
			type=float,
			dest='myfloat',
			help='This is help text for myfloat'
			)
		self.arg_parser.add_argument(
			'-e', '--myenum',
			type=str,
			dest='myselection',
			help='This is help text for myenum'
			)

	def effect(self):
		inkex.errormsg(f'mybool: {self.options.mybool}')
		inkex.errormsg(f'mystring: {self.options.mystring}')
		inkex.errormsg(f'myint: {self.options.myint}')
		inkex.errormsg(f'myfloat: {self.options.myfloat}')
		inkex.errormsg(f'selected item: {self.options.myselection}')
		inkex.errormsg(f'list of currently selected inkscape objects: {self.options.ids}')

if __name__ == '__main__':
	inx_tutorial = InxTutorial()
	inx_tutorial.run()

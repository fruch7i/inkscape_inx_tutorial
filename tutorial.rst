INX Basics
==========

Read input string
-----------------

In order to access a variable in python you need to:
  1. Create a ``param`` widget in the .inx file
  2. Parse the variable to the ``inkex.Effect`` class

Let us create a ``string`` parameter and parse the user input to our ``Effect`` class.

Inx file
^^^^^^^^

In the inx file, between the ``dependency`` and ``effect`` widgets, add a param widget, following this format:

.. code-block:: xml
  <param name="mystring" type="string" gui-text="This is mystring"></param>

.. note::
  Changes in your inx file only apply after restarting Inkscape. Restarting the extension itself is not sufficient.

Python file
^^^^^^^^^^^

In the python file, define the method ``add_arguments(self, pars)`` and parse the param value.
To do this, call the ``add_argument()`` method of ``pars``.
The first argument needs to match the ``name`` of the parameter in the inx file (with two leading minus signs).
It is good practice to specify the optional arguments ``type``, ``default`` and ``help``.

.. code-block:: python
  class InxTutorial(inkex.Effect):
    def add_arguments(self, pars):
      pars.add_argument("--mystring", type=str, default="",
        help="This is help text for mystring")

In order to see if everything worked as intended, let us give a simple output.
Add the ``effect()`` method and print the value of mystring as error message back to the user.
After successful parsing, you can access the value via self.options.PARAM_NAME, in this case self.options.mystring.

.. code-block:: python
  class InxTutorial(inkex.Effect):
    def effect(self):
      inkex.errormsg(f'mystring: {self.options.mystring}')

Now try to run your extension and return the error message ``Hello World!``.

.. note::
  Changes in your python file do not need a restart of Inkscape or the extension.

Read other variables
--------------------

Let us explore common variable types. We will add parameters of the following types:
  1) path
  2) bool
  3) integer
  4) float
  5) optiongroup
In addition, we will add a label and a header text.

Inx file
^^^^^^^^

In the inx file, between the ``dependency`` and ``effect`` widgets, add:

.. code-block:: xml
  <label appearance="header">This is a title in the popup </label>
  <label>This is some label for a description text.</label>
  <label>This is a new line in the description text.</label>
  <param name="mystring" type="string" gui-text="This is mystring"></param>
  <param name="mypath" type="path" mode="folder" gui-text="This is mypath"></param>
  <param name="mybool" type="boolean" gui-text="This is mybool"></param>
  <param name="myint" type="int" min="0" max="100" gui-text="This is myint"></param>
  <param name="myfloat" type="float" min="-100.0" max="100.0" gui-text="This is myfloat"></param>
  <param name="myoptiongroup" type="optiongroup" _gui-text="Select myoption:">
    <option value="first selection">first selection</option>
    <option value="second selection">second selection</option>
    <option value="another selection">another selection</option>
  </param>

.. note::
  Omiting ``min`` and ``max`` values for integer and float types defaults to 0 and 10, and 0.0 and 10.0 respectively.

Python file
^^^^^^^^^^^

In the python file, parse the other variables accordingly.

.. code-block:: python
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

.. note::
  Omitting ``type=inkex.Boolean`` for boolean parameters results in unexpected behaviour.
  This is due to ``XML`` saving all parameters as strings (``true``/``false``), while the python interpreter evaluates the non-empty string ``false`` as bool ``True``, without throwing an Exception.







BRAINSTORMING:
==============

The tutorial should explain how the .inx .py structure works:
(the following is how I understand it)
Inkscape interprets the .inx file, which defines the appearance and functionality of the extensions window.
When clicking apply, the python file in the <script> section of .inx file is called with all <param> values as arguments.
These arguments are handled by the add_arguments and add_argument methods and added as variables with the according names to self.options.PARAM_NAME automagically.
(this is done by the module argparse internally)
Finally, the effect() method of the inkex.Effect is called.

Noteable observations:
1) Changes on .inx files only take effect after restarting Inkscape, just restarting the extension does not work

2) Changes on .py files take immediate effect, no need to restart the extension or inkscape

3) XML handles bool values as strings (lowercase: true/false), thus inkex needs to convert them, which is nicely handled by inkex.Boolean.
This is important to know, since non empty strings are interpreted as True by python, so mistakes here do not throw an Exception, they just cause difficult to catch bugs.

4) Important locations and references for the tutorial, which should be located at https://inkscape-extensions-guide.readthedocs.io/en/latest/01_getting-started.html#
4)a) /home/USER/.config/inkscape/extensions/
4)b) /usr/share/inkscape/extensions/
4)c) https://gitlab.com/inkscape/extensions
4)d) there should be some link from here: https://inkscape.org/learn/tutorials/
4)e) there should be a basic overview wiki page here: https://wiki.inkscape.org/wiki/index.php?title=Inkscape

5) It would be cool if there was a HelloWorld extension among the core extensions. (submenu Tutorials?)
5)a) same is true for any future tutorial extension

6) Is there a thorough table of all .inx arguments/parameters/options somewhere?
I regularly stumble across new parameters like "indent", appearance="header", appearance="combo", "needs-live-preview" etc.,
but I don't know where to find one if I want to change something.
Is the following wiki page exhaustive?
https://wiki.inkscape.org/wiki/index.php?title=Extensions:_INX_widgets_and_parameters




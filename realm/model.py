from abc import ABC, abstractmethod
from inspect import cleandoc
import jinja2
import os
from jinja2 import Template

from realm.template import get_tex_template



# Something representable on paper
class Text(ABC):

    # used in filenames and such
    @abstractmethod
    def name(self):
        pass

    # returns a string containing LaTeX which represents the thing
    @abstractmethod
    def content_latex(self):
        pass

    # returns a string containing LaTeX on which the above method depends
    # stuff like '/usepackage' goes here
    @abstractmethod
    def preamble_latex(self, name_list=[]):
        pass

    def get_latex(self):
        template = get_tex_template(__file__, 'smalldoc.tex')
        return template.render(preamble = self.preamble_latex(), content=self.content_latex())

    def get_x_y_svg(self):
        pass

class Theorem(Text):

    def text_location(self):
        pass

    def name(self):
        pass

    @abstractmethod
    def hypotheses(self):
        pass

    @abstractmethod
    def goal(self):
        pass

    @abstractmethod
    def proof(self):
        pass

class World(ABC):

    @abstractmethod
    def objects(self):
        pass

    @abstractmethod
    def morphisms(self):
        pass

class Proof(ABC):

    @abstractmethod
    def from_world(self):
        pass

    @abstractmethod
    def to_world(self):
        pass


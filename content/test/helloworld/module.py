from realm.model import Text
from realm.template import get_tex_template

class HelloWorld(Text):

    def content_latex(self):
        return get_tex_template(__file__, 'content.tex').render()

    def preamble_latex(self):
        return get_tex_template(__file__, 'preamble.tex').render()

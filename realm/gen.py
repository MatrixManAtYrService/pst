from sh import pdflatex
import realm.constants as Constants

def makepdf(text):
    directory = Constants.tex_dir
    directory.mkdir(parents=True, exist_ok=True)
    file = (directory / (text.name() + '.tex')).absolute()
    with open(file, 'w') as f:
        f.write(text.get_latex())

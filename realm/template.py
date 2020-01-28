import jinja2
import pathlib



# loads a latex template from the directory that contains a given file
def get_template(py_file, template_file_name):

    jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(pathlib.Path(py_file).parent.absolute()))
    return latex_jinja_env.get_template(template_file_name)


# loads a latex template from the directory that contains a given file
# thaks to http://eosrei.net/articles/2015/11/latex-templates-python-and-jinja2-generate-pdfs
def get_tex_template(py_file, template_file_name):

    latex_jinja_env = jinja2.Environment(
            block_start_string = '\BLOCK{',
            block_end_string = '}',
            variable_start_string = '\VAR{',
            variable_end_string = '}',
            comment_start_string = '\#{',
            comment_end_string = '}',
            line_statement_prefix = '%%',
            line_comment_prefix = '%#',
            trim_blocks = True,
            autoescape = False,
            loader = jinja2.FileSystemLoader(pathlib.Path(py_file).parent.absolute())
    )
    return latex_jinja_env.get_template(template_file_name)


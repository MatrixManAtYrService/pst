from setuptools import setup
setup(name='slicetool',
            version='0.1.0.dev1',
            description='A structural experiment involving axioms',
            url='https://github.com/MatrixManAtYrService/pst',
            author='Matt Rixman',
            author_email='github@matt.rixman.org',
            packages=['pst'],
            python_requires= '>=3.6',
            install_requires=['sh', 'pymysql', 'pdflatex', 'jinja2', 'tinydb'],
            entry_points={'console_scripts' : [

                          # generate a document by name
                          'generate = pst.generate:main',

                          # list stored documents
                          'list = pst.list:main',

                          ]})

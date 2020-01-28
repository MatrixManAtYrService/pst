from setuptools import setup
setup(name='realm',
            version='0.1.0.dev1',
            description='Consider a graph where the edges are theorems...',
            url='https://github.com/MatrixManAtYrService/pst',
            author='Matt Rixman',
            author_email='github@matt.rixman.org',
            packages=['realm', 'content'],
            python_requires= '>=3.6',
            install_requires=['sh', 'jinja2', 'pytest'],
            entry_points={'console_scripts' : [

                          # generate a document by name
                          'generate = pst.generate:main',

                          # list stored documents
                          'list = pst.list:main',

                          ]})

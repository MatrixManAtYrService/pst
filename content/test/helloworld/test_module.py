from content.test.helloworld import HelloWorld
from realm.gen import makepdf

def test_hello():
    obj = HelloWorld()
    print(obj.get_latex())

def test_pdf():
    obj = HelloWorld()
    makepdf(obj)


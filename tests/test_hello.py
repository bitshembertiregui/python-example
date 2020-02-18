import hello


def test_says_world():
    assert hello.say_what() == 'world'

def test_says_hello():
	print(hello.say_what())
	print(hello.hello(hello.say_what()))
    assert hello.hello(hello.say_what()) == 'Hello, world!'

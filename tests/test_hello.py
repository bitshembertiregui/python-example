import hello


def test_says_world():
    assert hello.say_what() == 'world'

def test_says_hello():
	hello.hello(hello.say_what())

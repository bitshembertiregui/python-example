import hello


def test_says_world():
    assert hello.say_what() == 'world'

def test_says_hello():
    assert hello.hello(hello.say_what()) == 'Hello, world!'

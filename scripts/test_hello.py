from scripts.hello import say_hello


def test_say_hello():
    assert say_hello() == "Hello, World!", "Your function is wrong"

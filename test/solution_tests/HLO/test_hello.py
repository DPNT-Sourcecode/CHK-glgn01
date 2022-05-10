from solutions.HLO import hello_solution


class TestHlo():
    def test_hello(self):
        name = 'Yohan'
        assert hello_solution.hello(name) == 'Hello, World!'


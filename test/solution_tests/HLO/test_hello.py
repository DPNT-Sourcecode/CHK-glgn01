from solutions.HLO import hello_solution


class TestHlo():
    def test_hello(self):
        name = 'Yohan'
        result = hello_solution.hello(name)
        assert False if result.find(name) == -1 else True

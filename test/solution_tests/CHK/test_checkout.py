from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):

        assert checkout_solution.checkout('Abbc') == -1
        assert checkout_solution.checkout('ABB') == 95
        assert checkout_solution.checkout('Ab6c*') == -1
        assert checkout_solution.checkout('AAAAAAABBCCD') == 410
        assert checkout_solution.checkout(334) == -1
        assert checkout_solution.checkout('ABBCNNDKK') == -1
        assert checkout_solution.checkout('ABBBBBBCDDEEEEEEEEEEEE') == 580



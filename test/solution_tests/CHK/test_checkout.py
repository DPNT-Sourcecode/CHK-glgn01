from solutions.CHK import checkout_solution


class TestCHK():
    def test_checkout(self):

        assert checkout_solution.checkout('Abbc') == -1
        assert checkout_solution.checkout('ABB') == 95
        assert checkout_solution.checkout('Ab6c*') == -1
        assert checkout_solution.checkout('AAAAAAABBCCD') == 400
        assert checkout_solution.checkout(334) == -1
        assert checkout_solution.checkout('ABBCNNDKK') == 360
        assert checkout_solution.checkout('ABBBBBBCDDEEEEEEEEEEEE') == 580
        assert checkout_solution.checkout('EE') == 80
        assert checkout_solution.checkout('EEB') == 80
        assert checkout_solution.checkout('EEEB') == 120
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout('AAAAAAA') == 300
        assert checkout_solution.checkout("EEEEBB")==160
        assert checkout_solution.checkout("BEBEEE")==160
        assert checkout_solution.checkout("A")== 50
        assert checkout_solution.checkout("AA")==100
        assert checkout_solution.checkout("AAA")==130
        assert checkout_solution.checkout("AAAA")==180
        assert checkout_solution.checkout("AAAAA")== 200
        assert checkout_solution.checkout("AAAAAA")==250
        assert checkout_solution.checkout("B")== 30
        assert checkout_solution.checkout("BB")==45
        assert checkout_solution.checkout("BBB")== 75
        assert checkout_solution.checkout("BBBB")==90
        assert checkout_solution.checkout("FF")==20
        assert checkout_solution.checkout("FFF")== 20
        assert checkout_solution.checkout("FFFF")== 30
        assert checkout_solution.checkout("FFFFFF") == 40
        assert checkout_solution.checkout("AABBDLKLLNHGGGGFFFBVVVVV")== 910



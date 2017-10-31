import unittest
import SMATINY
import SMETANA

class Test_examples(unittest.TestCase):

    def test_SMETANA_HelloWorld(self):

        code = """1. Swap 1 with 71.
10. Output this block's position.
11. Swap 11 with 150.
32. Output this block's position.
34. Swap 33 with 32.
35. Swap 35 with 118.
36. Swap 36 with 9.
72. Output this block's position.
101. Output this block's position.
102. Swap 101 with 100.
103. Swap 103 with 107.
104. Swap 104 with 32.
108. Output this block's position.
109. Swap 109 with 107.
111. Output this block's position.
112. Swap 112 with 31.
114. Output this block's position.
115. Swap 110 with 117.
116. Swap 116 with 107.
117. Swap 110 with 99.
119. Output this block's position.
120. Swap 120 with 110.
"""
        outstr = SMATINY.interpret(code)
        self.assertEqual(outstr, "Hello world!\n")

    def test_SMETANA_simple(self):
        code = """Step 1. Swap step 1 with step 3.
Step 2. Go to step 3.
Step 3. Go to step 3.
"""
        final_state = SMETANA.interpret(code)
        self.assertEqual(final_state, {1: 3, 2: 3, 3: [1, 3]})

if __name__ == '__main__':
    unittest.main()

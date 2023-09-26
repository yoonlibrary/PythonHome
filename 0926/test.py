#import unittest
#import myfunction           #같은 디렉터리, py 생략

#class Mytest(unittest.TestCase) :
#    def test_sum(self) :
#        self.assertEqual(myfunction.sum(2,5), 7)
    
#    def test_multiple(self) :
#        self.assertEqual(myfunction.multiple(2,5), 9)

import myfunction

def test_sum() :
    assert myfunction.sum(2,5) == 7    #assert 뒤에는 참/거짓 문장
    assert myfunction.sum(2.5,5.2) == 7.7
    
def test_multiple() :
    assert myfunction.multiple(2,5) == 10
    assert myfunction.multiple(2.0,5.0) == 10.0
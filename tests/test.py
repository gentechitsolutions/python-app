from src.math import add, sub

def add_test():
    assert add(2,3)==5
    assert add(1,5)==6
    assert add(-1,5)==4

def sub_test():
    assert sub(2,3)==-1
    assert sub(4,3)==1
    assert sub(2,-3)==1
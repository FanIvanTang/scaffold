from hello import add

def test_add_1():
    
    assert add(1,2)==3
    
def test_add_2():
    assert add(-1,1)==0
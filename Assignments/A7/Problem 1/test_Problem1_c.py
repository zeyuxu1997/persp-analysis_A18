import Problem1_c, pytest
def test_cases():
    assert Problem1_c.operate(1,2,"+") == 3, "False Function"
    assert Problem1_c.operate(1,2,"-") == -1, "False Function"
    assert Problem1_c.operate(1,2,"*") == 2, "False Function"
    assert Problem1_c.operate(1,2,"/") == 0.5, "False Function"
    pytest.raises(ZeroDivisionError, Problem1_c.operate, a=1, b=0, oper='/')
    pytest.raises(TypeError, Problem1_c.operate, a=1, b=1, oper=1)
    pytest.raises(ValueError, Problem1_c.operate, a=1, b=1, oper="1")
    
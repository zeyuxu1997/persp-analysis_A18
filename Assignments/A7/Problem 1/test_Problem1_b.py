import Problem1_b
def test_cases():
    assert Problem1_b.month_length("September") == 30, "False Function"
    assert Problem1_b.month_length("March") == 31, "False Function"
    assert Problem1_b.month_length("February") == 28, "False Function"
    assert Problem1_b.month_length("February", leap_year = True) == 29, "False Function"
    assert Problem1_b.month_length(3) == None, "False Function"
from janken import int2hand
from janken import judge

def test_int2hand_1():
    expected = 'グー'
    actual = int2hand(1)
    assert expected == actual

def test_int2hand_2():
    expected = 'チョキ'
    actual = int2hand(2)
    assert expected == actual

def test_int2hand_3():
    expected = 'パー'
    actual = int2hand(3)
    assert expected == actual

def test_judge_3_1():
    expected = 'user'
    actual = judge(3,1)
    assert expected == actual

def test_judge_1_2():
    expected = 'computer'
    actual = judge(1,2)
    assert expected == actual

def test_judge_2_2():
    expected = 'draw'
    actual  = judge(2,2)
    assert expected == actual
from app import swap

def test_length_to_swap():
    assert swap.length_to_swap("Donald") == 1
    assert swap.length_to_swap("Doonald") == 2
    assert swap.length_to_swap("oonald") == 1
    assert swap.length_to_swap("oo") == 1

def test_get_new_words(): 
    assert swap.get_new_words("aa","oo") == ('oo', 'aa')

def test_change_words():
    assert swap.change_words("aa oo") == "oo aa"
    assert swap.change_words("aa oo aa ii") == "oo aa ii aa"
import main

def test_endOfSwap():
    assert main.endOfSwap("Donald") == 1
    assert main.endOfSwap("Doonald") == 2
    assert main.endOfSwap("oonald") == 1
    assert main.endOfSwap("oo") == 1

def test_newWords(): 
    assert main.newWords("aa","oo") == ('oo', 'aa')

def test_change_words():
    assert main.change_words("aa oo", ["aa","oo"]) == "oo aa"
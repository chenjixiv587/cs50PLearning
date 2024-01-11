from twttr import shorten

def test_upper():
    assert shorten("AEIOUhjs") == "hjs"
def test_lower():
    assert shorten("aeiouhjs") == "hjs"


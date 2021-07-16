from snake.md import InlineText

def test_inline_text_empty():
    text = InlineText("")
    assert text.text == ""
    assert str(text) == ""

def test_inline_text_str():
    text = InlineText("Hello, World!")
    assert text.text == "Hello, World!"
    assert str(text) == "Hello, World!"

def test_inline_text_bold():
    text = InlineText("Hello, World!", bold=True)
    assert text.text == "Hello, World!"
    assert str(text) == "**Hello, World!**"

def test_inline_text_italics():
    text = InlineText("Hello, World!", italics=True)
    assert text.text == "Hello, World!"
    assert str(text) == "*Hello, World!*"

def test_inline_text_bold_italics():
    text = InlineText("Hello, World!", italics=True, bold=True)
    assert text.text == "Hello, World!"
    assert str(text) == "***Hello, World!***"

def test_inline_text_code():
    text = InlineText("x = 7", code=True)
    assert text.text == "x = 7"
    assert str(text) == "`x = 7`"

def test_inline_text_url():
    text = InlineText("Here", url="https://google.com")
    assert text.text == "Here"
    assert text.url == "https://google.com"
    assert str(text) == "[Here](https://google.com)"

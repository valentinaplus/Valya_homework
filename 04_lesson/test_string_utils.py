import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


class TestStringUtils:
    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("SkyPro", "Skypro"),
        ("", ""),
        ("1test", "1test"),
        ("data", "Data"),
        ("m", "M"),
        ("UPPERCASE", "Uppercase"),
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("bad_input", [
        None,
        123,
        [],
        {},
        b"bytes",
        3.14,
        (1, 2),
    ])
    def test_capitalize_negative(self, utils, bad_input):
        with pytest.raises(TypeError):
            utils.capitalize(bad_input)

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("Hello World", " ", "HelloWorld"),
        ("test", "x", "test"),
        ("", "a", ""),
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol", [
        (None, "a"),
        ("abc", None),
        (123, "a"),
        ("abc", 5),
    ])
    def test_delete_symbol_negative(self, utils, string, symbol):
        with pytest.raises((AttributeError, TypeError)):
            utils.delete_symbol(string, symbol)

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "y", True),
        ("", "", True),
        ("abc", "", True),
        ("abc", "z", False),
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        assert utils.contains(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol", [
        (None, "a"),
        ("abc", None),
        (123, "a"),
        ("abc", 5),
    ])
    def test_contains_negative(self, utils, string, symbol):
        with pytest.raises((AttributeError, TypeError)):
            utils.contains(string, symbol)

    @pytest.mark.parametrize("input_str, expected", [
        ("   leading spaces", "leading spaces"),
        ("no leading", "no leading"),
        ("      ", ""),
        ("", ""),
        ("  mixed  spaces ", "mixed  spaces "),
    ])
    def test_trim_positive(self, utils, input_str, expected):
        assert utils.trim(input_str) == expected

    @pytest.mark.parametrize("bad_input", [
        None,
        123,
        ["   "],
    ])
    def test_trim_negative(self, utils, bad_input):
        with pytest.raises(TypeError):
            utils.trim(bad_input)

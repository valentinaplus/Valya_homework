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
    ])
    def test_capitalize_positive(self, utils, input_str, expected):
        assert utils.capitalize(input_str) == expected

    def test_capitalize_negative(self, utils):
        with pytest.raises(AttributeError):
            utils.capitalize(None)

        with pytest.raises(TypeError):
            utils.contains("abc", None)

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("Hello World", " ", "HelloWorld"),
        ("test", "x", "test"),
        ("", "a", ""),
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        assert utils.delete_symbol(string, symbol) == expected

    def test_delete_symbol_negative(self, utils):
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

        with pytest.raises(TypeError):
            utils.delete_symbol("abc", None)

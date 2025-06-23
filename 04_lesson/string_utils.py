class StringUtils:
    def capitalize(self, string: str) -> str:
        if not isinstance(string, str):
            raise TypeError("string must be of type str")
        return string.capitalize()

    def trim(self, string: str) -> str:
        if not isinstance(string, str):
            raise TypeError("string must be of type str")
        return string.lstrip()

    def contains(self, string: str, symbol: str) -> bool:
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("arguments must be of type str")
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        if not isinstance(string, str) or not isinstance(symbol, str):
            raise TypeError("arguments must be of type str")
        return string.replace(symbol, "")

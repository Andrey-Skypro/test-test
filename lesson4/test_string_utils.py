from string_utils import StringUtils
import pytest


@pytest.mark.parametrize( "word, result_word", [ ("слово", "Слово"), ("123456", "123456"), ("№;%:", "№;%:"), ("大友克洋武器よさらば", "大友克洋武器よさらば"),
                                                 ("the doctor never so much as moved", "The doctor never so much as moved"), 
                                                 # добавлена проверка с предложением в качестве пареметра
                                                  (", as before, over his shoulder", ", as before, over his shoulder"), # проверка со строкой начинающейся со спецсимвола
                                                  (" ", " ")] # проверка со строкой из пробелов 
                                                  ) 
def test_capitilize(word, result_word):
    stringUtils=StringUtils()
    result=stringUtils.capitilize(word)
    assert result == result_word, "ожидаемый результат не равен фактическому:"
    
@pytest.mark.xfail()
@pytest.mark.parametrize( "word, result_word", [ (12345, 12345), ( [], [] ), (None, "skypro"), (" ", "skypro")]) 
def test_capitilize_negative(word, result_word):
    stringUtils=StringUtils()
    result=stringUtils.capitilize(word)
    assert result == result_word, "ожидаемый результат не равен фактическому:"


# Тестирование позитивных сценариев
@pytest.mark.parametrize("word, result_word", [
    ("слово", "Слово"),
    ("SKYPRO", "Skypro"),
    ("Sky pro", "Sky pro"),
    ("SkyPro", "Skypro"),
    ("123", "123"),
    ("04 апреля 2023", "04 апреля 2023")
])
def test_capitalize_positive(word, result_word):
    stringUtils = StringUtils()
    result = stringUtils.capitalize(word)
    assert result == result_word, f"ожидаемый результат {result_word} не равен фактическому: {result}"

# Тестирование негативных сценариев (здесь для негативных сценариев мы комментируем, так как в задании были неверные ожидания)
# Будем считать тест негативным, если функция ведет себя не так, как мы ожидаем. Но функция capitalize изначально не предполагает "негативного" результата - она просто изменяет входящее значение.
# Тут мы тестируем граничные случаи и поведение функции при "некорректном" вводе.
@pytest.mark.parametrize("word", ["", " "])
def test_capitalize_empty_and_space(word):
    stringUtils = StringUtils()
    result = stringUtils.capitalize(word)
    assert result == word, f"Функция capitalize должна возвращать исходную строку для '{word}'"

# Граничные случаи
@pytest.mark.parametrize("word", [None, []])
def test_capitalize_none_and_empty_list(word):
    stringUtils = StringUtils()
    with pytest.raises((TypeError, AttributeError)):
        # Ожидаем ошибку, так как None и [] - недопустимые значения для данной функции
        stringUtils.capitilize(word)

class TestStringUtils:
    @pytest.mark.parametrize("word, result_word", [
        ("слово", "Cлово"),
        ("123456", "123456"),
        ("№;%:", "№;%:"),
        ("大友克洋武器よさらば", "大友克洋武器よさらば"),
        ("the doctor never so much as moved", "The doctor never so much as moved"),
        (", as before, over his shoulder", ", as before, over his shoulder"),
        (" ", " ")
    ])
    def test_trim(self, word, result_word):
        stringUtils = StringUtils()
        result = stringUtils.trim(word)
        assert result == result_word, "ожидаемый результат не равен фактическому:"  

import pytest
from string_utils import StringUtils

class TestStringUtils:
    @pytest.mark.parametrize("word, result_word", [
        ("слово", "Слово"),
        ("123456", "123456"),
        ("№;%:", "№;%:"),
        ("大友克洋武器よさらば", "大友克洋武器よさらば"),
        ("the doctor never so much as moved", "The doctor never so much as moved"),
        (", as before, over his shoulder", ", as before, over his shoulder"),
        (" ", " ")
    ])
    def test_to_list(self, word, result_word):
        stringUtils = StringUtils()
        result = stringUtils.to_list(word)
        assert result == result_word, "ожидаемый результат не равен фактическому:"

@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("Привет, мир!", ",", True),
        ("Тестирование", "т", False),
        ("123456", "5", True),
        (" ", " ", True),
    ]
)
def test_contains(string, symbol, expected):
    result = contains(string, symbol)
    assert result == expected

def contains(string: str, symbol: str) -> bool:
    try:
        return string.index(symbol) > -1
    except ValueError:
        return False   

@pytest.mark.parametrize(
    "string, symbol, expected",
    
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("Привет, мир! Как дела?", ",", "Привет мир! Как дела?"),
        ("Тестирование", "т", "Тесирование"),
        ("123456", "5", "12346"),
        (" ", " ", ""),
    
)
def testdeletesymbol(string, symbol, expected):
    result = deletesymbol(string, symbol)
    assert result == expected

def deletesymbol(string: str, symbol: str) -> str:
    if contains(string, symbol):
        return string.replace(symbol, "")
    else:
        return string

def contains(string: str, symbol: str) -> bool:
    return string.find(symbol) != -1

@pytest.mark.parametrize(
    "string, symbol, expected",
    
        ("SkyPro", "S", True),
        ("SkyPro", "P", False),
        ("Привет, мир!", "П", True),
        ("Тестирование", "т", True),
        ("123456", "1", True),
        (" ", " ", True),
    
)
def teststartswith(string, symbol, expected):
    result = startswith(string, symbol)
    assert result == expected

def startswith(string: str, symbol: str) -> bool:
    return string.startswith(symbol)

@pytest.mark.parametrize(
    "string, symbol, expected",
    
        ("SkyPro", "o", True),
        ("SkyPro", "y", False),
        ("Привет, мир!", "!", True),
        ("Тестирование", "е", False),
        ("123456", "6", True),
        (" ", " ", True),
    
)
def testendwith(string, symbol, expected):
    result = endwith(string, symbol)
    assert result == expected

def endwith(string: str, symbol: str) -> bool:
    return string.endswith(symbol)

@pytest.mark.parametrize(
    "string, expected",
    
        ("", True),
        (" ", True),
        ("SkyPro", False),
        (" Привет, мир!", False),
        ("123456", False),
    
)
def testisempty(string, expected):
    result = isempty(string)
    assert result == expected

def isempty(string: str) -> bool:
    return string.strip() == ""

@pytest.mark.parametrize(
    "lst, joiner, expected",
    [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["Sky", "Pro"], ", ", "Sky, Pro"),
        (["Sky", "Pro"], "-", "Sky-Pro"),
        ([], ", ", ""),
        (["Привет", "мир", "как", "дела?"], " ", "Привет мир как дела?"),
        (["1", "2", "3"], "/", "1/2/3"),
    ]
)
def test_list_to_string(lst, joiner, expected):
    result = list_to_string(lst, joiner)
    assert result == expected

def list_to_string(lst: list, joiner: str = ", ") -> str:
    return joiner.join(map(str, lst))                 



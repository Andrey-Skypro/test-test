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
    
#@pytest.mark.xfail()
@pytest.mark.parametrize( "word, result_word", [ (12345, 12345),( [], [] )]) 
def test_capitilize_negative(word, result_word):
    stringUtils=StringUtils()
    result=stringUtils.capitilize(word)
    assert result == result_word, "ожидаемый результат не равен фактическому:"

import pytest
from string_utils import StringUtils

# Тестирование позитивных сценариев
@pytest.mark.parametrize("word, result_word", [
    ("слово", "Слово"),
    ("SKYPRO", "Skypro"),
    ("Sky pro", "Sky pro"),
    ("SkyPro", "Skypr"),
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
        stringUtils.capitalize(word)

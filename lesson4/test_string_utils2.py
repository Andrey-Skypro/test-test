from string_utils import StringUtils
import pytest
class TestStringUtils:

 @pytest.mark.parametrize( "word, result_word", [ ("слово", "Слово"), ("123456", "123456"), ("№;%:", "№;%:"), ("大友克洋武器よさらば", "大友克洋武器よさらば"),
                                                 ("the doctor never so much as moved", "The doctor never so much as moved"), 
                                                 # добавлена проверка с предложением в качестве пареметра
                                                  (", as before, over his shoulder", ", as before, over his shoulder"), # проверка со строкой начинающейся со спецсимвола
                                                  (" ", " ")] # проверка со строкой из пробелов 
                                                  ) 
 def test_capitalize(self, word, result_word):
    stringUtils=StringUtils()
    result=stringUtils.capitalize(word)
    assert result == result_word, "ожидаемый результат не равен фактическому:"
    
@pytest.mark.xfail()
@pytest.mark.parametrize("word, result_word", [ (12345, 12345), ( [], [] ), ("None", "None"), (" ", " ")]) 
def test_capitalize_negative(self, word, result_word):
    stringUtils=StringUtils()
    result=stringUtils.capitilize(word)
    assert result == result_word, "ожидаемый результат не равен фактическому:"

    def test_capitalize_empty_and_space(word):
     stringUtils=StringUtils()
    result = stringUtils.capitilize(word)
    assert result == word, f"Функция capitalize должна возвращать исходную строку для '{word}'"

    @pytest.mark.parametrize("word", [None, []])
    def test_capitalize_none_and_empty_list(word):
     stringUtils = StringUtils()
    with pytest.raises((TypeError, AttributeError)):
        # Ожидаем ошибку, так как None и [] - недопустимые значения для данной функции
        stringUtils.capitilize(word)

        def test_trim(self, word, result_word):
         stringUtils = StringUtils()
        result = stringUtils.trim(word)
        assert result == result_word, "ожидаемый результат не равен фактическому:"     

def test_to_list(self, word, result_word):
        stringUtils = StringUtils()
        result = stringUtils.to_list(word)
        assert result == result_word, "ожидаемый результат не равен фактическому:"

def teststartswith(string, symbol, expected):
    result = startswith(string, symbol)
    assert result == expected

def startswith(string: str, symbol: str) -> bool:
    return string.startswith(symbol)

def testendwith(string, symbol, expected):
    result = endwith(string, symbol)
    assert result == expected

def endwith(string: str, symbol: str) -> bool:
    return string.endswith(symbol)

def testisempty(string, expected):
    result = isempty(string)
    assert result == expected

def isempty(string: str) -> bool:
    return string.strip() == ""

def test_list_to_string(lst, joiner, expected):
    result = list_to_string(lst, joiner)
    assert result == expected

def list_to_string(lst: list, joiner: str = ", ") -> str:
    return joiner.join(map(str, lst))  
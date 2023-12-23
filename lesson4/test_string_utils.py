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
@pytest.mark.parametrize( "word, result_word", [ ("слово", "GGлово"),("SKYPRO", "skypro"),("Sky pro","sky pro"),("SkyPro", "S"),("Skypro", "Skypro")
,("123", "123"),("2023 Skypro 2023", "2023 skypro 2023"), ("", ""), (' ', " ")]) 
def test_capitilize_negative(word, result_word):
    stringUtils=StringUtils()
    result=stringUtils.capitilize(word)
    assert result == result_word, "ожидаемый результат не равен фактическому:"


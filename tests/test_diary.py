from lib.diary_class import *
import pytest 

"""
without any diary entry list is also empty. 
"""
def test__initaly_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

"""
initally world count is zero 
"""
def test__initaly_reading_time():
    diary = Diary()
    assert diary.count_words() == 0
"""
initally, #reading_time should raise an error 
"""
def test__initaly_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2) 
    assert str(err.value) == "No entries is given to read"

# """
# initally #find_the_best_entry_for_reading_time should raise an error message
# """
def test__initaly_best_entry_for_reading():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.find_best_entry_for_reading_time(2,1)
    assert str(err.value) == "No entries is given to read"



from lib.diary_class import *
from lib.diary_entry_class import *

"""
given two diary entry and 
add them in the diary and 
list them. 
"""
def test_add_two_entries_and_list_them():
    diary = Diary() 
    entry_1 = DiaryEntry("morning","breakfast ready")
    entry_2 = DiaryEntry("afternoon","have lunch ")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]


"""
given I add two diary entries 
and count all words
I get the sum of all words in the contents of the diary entries
"""

def test_add_two_entries_and_count_all_words():
    diary = Diary()
    entry_1 = DiaryEntry("morning","breakfast ready")
    entry_2 = DiaryEntry("afternoon","have lunch ready ")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

"""
given I add two diary entries,one long and one sort
with given wpm and minutes that means I can only read the sort one. 
then find the best one is shorter one return.  
"""

def test_find_the_entry_for_reading_in_given_time():
    diary = Diary()
    entry_1 = DiaryEntry("morning","breakfast ready")
    entry_2 = DiaryEntry("afternoon","one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2,3) == entry_1

"""
given I add two diary entries,both are more than readable with given wpm and minutes that means I can't read any entires and return none.   
"""

def test_entries_more_than_given_wpm_and_minutes():
    diary = Diary()
    entry_1 = DiaryEntry("morning","breakfast ready one two three four five")
    entry_2 = DiaryEntry("afternoon","one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2,3) == None

"""
Given I add two diary entries
And I call #find_best_entry_for_reading_time
with a wpm and miniutes that means I could rad both
Then #find_best_entry_for_reading_time return the longest one. 
"""
def test_no_list_cannot_read_in_given_time():
    diary = Diary()
    entry_1 = DiaryEntry("morning","breakfast ready one two three")
    entry_2 = DiaryEntry("afternoon","one two three four ")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2,3) == entry_1
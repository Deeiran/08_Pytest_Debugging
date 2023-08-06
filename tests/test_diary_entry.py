from lib.diary_entry_class import *

"""
When I initialise the title and contents 
Ican get that titel and contents in properties
"""
def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry("morning","breakfast ready")
    assert diary_entry.title == "morning"
    assert diary_entry.contents == "breakfast ready"
    
"""
when I instialise contents with five words
the count words should return five
"""
def test_content_with_five_words():
    diary_entry = DiaryEntry("morning","breakfast ready one two three")
    assert diary_entry.count_words() == 5

"""
when I instialise contents with four words
and wpm is 2
the count words should return 2
"""
def test_reading_time_for_five_words_two_wpm():
    diary_entry = DiaryEntry("morning","breakfast ready one two three")
    assert diary_entry.reading_time(2) == 3

"""
when I instialise contents with six words
then,at first,#reading chunk should return first chunk readable in given minutes        
"""
def test_readable_chunk_for_six_words_two_wpm():
    diary_entry = DiaryEntry("morning","breakfast ready one two three four")
    assert diary_entry.reading_chunk(2,1) == "breakfast ready"

"""
when I instialise contents with six words
then,on the second call  #reading chunk should return second chunk readable in given minutes        
"""
def test_readable_chunk_in_second_call():
    diary_entry = DiaryEntry("morning","breakfast ready one two three four")
    assert diary_entry.reading_chunk(2,1) == "breakfast ready"
    assert diary_entry.reading_chunk(2,1) == "one two"

"""
when I instialise contents with five words
then,call third times  #reading chunk should return second chunk readable in given minutes        
"""
def test_readable_chunk_in_third_call():
    diary_entry = DiaryEntry("morning","breakfast ready one two three")
    assert diary_entry.reading_chunk(2,1) == "breakfast ready"
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,1) == "three" 
"""
when I instialise contents with five words
then,call fourth times  #reading chunk should return should read from the begining in given minutes        
"""
def test_readable_chunk_to_check_from_beginning():
    diary_entry = DiaryEntry("morning","breakfast ready one two three")
    assert diary_entry.reading_chunk(2,1) == "breakfast ready"
    assert diary_entry.reading_chunk(2,1) == "one two"
    assert diary_entry.reading_chunk(2,1) == "three" 
    assert diary_entry.reading_chunk(2,1) == "breakfast ready"


 
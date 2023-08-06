from lib.music_library import *
from lib.tracker import *

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_add_two_tracks_and_list_them():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.all() == [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
def test_add_two_tracks_search_by_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Always The Hard Way") == [track_1] 

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
def test_search_by_part_of_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("Place") == [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
def test_track_not_in_the_list():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title("zzz") == []


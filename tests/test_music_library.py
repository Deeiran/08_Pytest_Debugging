from lib.music_library import *

"""
there is no tracks in the list at start. 
"""
def test_empty_tracks_at_start():
    library = MusicLibrary()
    assert library.all() == []
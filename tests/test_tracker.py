from lib.tracker import *

"""
when we create a new track 
we can get its title and artist back
"""
def test_create_new_track_get_title_and_artist():
    track = Track("Always The Hard Way", "Terror")
    assert track.title == "Always The Hard Way"
    assert track.artist == "Terror"

"""
format the track with title and artist
"""
def test_format_the_track():
    track =Track("My Title","My Artist")
    assert track.format() == "My Title, My Artist"


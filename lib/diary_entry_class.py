import math
class DiaryEntry:
    def __init__(self, title, contents): 
            self.title = title
            self.contents = contents
            self.start_point = 0

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return math.ceil(self.count_words()/wpm)
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
    
    def reading_chunk(self, wpm, minutes):
        readable_words_in_given_time = wpm * minutes
        words = self.contents.split()
        if len(words) <= self.start_point:
             self.start_point = 0
        end_point = self.start_point + readable_words_in_given_time
        readable_chunk =  " ".join(words[self.start_point:end_point])
        self.start_point += readable_words_in_given_time
        return readable_chunk
        
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.

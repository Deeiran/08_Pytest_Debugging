from math import ceil
class Diary:
    def __init__(self):
        self.list_entries = []

    def add(self, entry):
        self.list_entries.append(entry)
  

    def all(self):
        return self.list_entries


    def count_words(self):
        words_counts = [entry.count_words()for entry in self.list_entries] 
        return sum(words_counts)   
            # for entry in self.list_entries:
            #     total += entry.count_words
            # return total

    def reading_time(self, wpm):
        if self.list_entries == []:
            raise Exception("No entries is given to read")
        return ceil(self.count_words()/wpm)
    

        # Parameters:
        #   wpm: an integer representing the number of words the user can   read
        #   per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
    
    def find_best_entry_for_reading_time(self, wpm, minutes):
        if self.list_entries == []:
            raise Exception("No entries is given to read")
        chunk_readable_words_in_given_min = wpm * minutes
        readable_entry = None
        longest_readable_words = 0
        for entry in self.list_entries:
            if entry.count_words() <= chunk_readable_words_in_given_min:
                if entry.count_words() > longest_readable_words:
                    readable_entry = entry
                    longest_readable_words = entry.count_words()
        return readable_entry

        # Parameters:
        #   wpm:     an integer representing the number of words the use can read per minute
        #   minutes: an integer representing the number of minutes the user has to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.


        
   



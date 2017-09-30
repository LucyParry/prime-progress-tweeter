import random

def get_random_line(filepath):
   """
   Returns a random line from a given .txt file using a reservoir sampling algorithm (the lists probably
   won't be large enough to make a noticeable difference but here it is for the sake of learning a New Thing)
   This video explains the algorithm simply (with hats!) - https://www.youtube.com/watch?v=A1iwzSew5QY
   Code example - https://jeremykun.com/2013/07/05/reservoir-sampling/
   """
   selection = ""
   with open(filepath) as file:
      for i, linetext in enumerate(file, start=1):
         if random.randrange(i) == 0:
               selection = linetext
   return selection.replace("\n", "")

class Exclamation:
   """
   An absurd, randomly generated exclamation suitable for excited tweeting
   """
   def __init__(self, special = False):
      if special:
          self.text = get_random_line('wordlists/short_phrases.txt')
      else:  
        exclamation_starts_list = ["Great", "Holy", "Sweet", "Oh my", "Damn this", "What the", "Bless my"]
        start, adjective, noun, text = "", "", "", ""

        self.start = exclamation_starts_list[(random.randrange(0, (len(exclamation_starts_list))))]
        self.adjective = get_random_line('wordlists/adjectives.txt')
        self.noun = get_random_line('wordlists/nouns.txt')
        self.text = self.start + " " + self.adjective + " " + self.noun + "!"
        if self.start == "What the":
            self.text += "?"




from random import choice

QUOTE_DATA = [
  [
    "You can’t cross the sea merely by standing and staring at the water", "Rabindranath Tagore"
  ],
  [
    "There is a wisdom of the head, and a wisdom of the heart",
    "Charles Dickens"
  ],
  [
    "Art ought never to be considered except in its relations with its ideal beauty",
    "Alfred de Vigny"
  ],
  [
    "In the world of words, the imagination is one of the forces of nature", "Wallac"
  ],
  [
    "Communism is like one big phone company",
    "Lenny Bruce"
  ],
  [
    "Sweet mercy is nobility's true badge",
    "Williams Shakespeare"
  ]
]

def return_random_quote():
  quote_author_sep = choice(QUOTE_DATA)
  return f"{quote_author_sep[0]} - {quote_author_sep[1]}"

print(return_random_quote())
  
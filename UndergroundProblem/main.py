VICTORIA_LINE = [
  "Brixton", "Stockwell", "Vauxhall", 
  "Pimlico", "Victoria", "Green Park", 
  "Oxford Circus", "Warren Street", "Euston", 
  "King's Cross", "Highbury & Islington", "Finsbury Park", 
  "Seven Sisters", "Tottenham Hale", "Blackhorse Road", 
  "Walthamstow Central."
]


def distance_between(*, station1: str, station2: str):
  """
  Find the distance between the two stops, expressed as 
  the number of stops station2 is away from station1.
  """
  
  s1_index = VICTORIA_LINE.index(station1.title())
  s2_index = VICTORIA_LINE.index(station2.title())

  return s2_index - s1_index

print(
  distance_between(
    station1="brixton",
    station2="Euston"
  )
)

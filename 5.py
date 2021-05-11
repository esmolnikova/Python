from random import sample
def get_jokes(k):
   """Create list from k random jokes from three list verbs"""
   jokes = []
   nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
   adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
   adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

   n = sample(nouns, k)
   adv = sample(adverbs, k)
   adj = sample(adjectives, k)

   for nn, advv, adjj in zip(n, adv, adj):
      jokes.append(f'{nn} {advv} {adjj}')
   print(jokes)


get_jokes(2)


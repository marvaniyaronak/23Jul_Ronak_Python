def match_words(words):
  cr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      cr += 1
  return cr

print(match_words(['abc', 'xyx', 'abe', '1221']))

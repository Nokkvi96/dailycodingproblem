import numpy as np

# TODO make it work if m and n is not equal
def shortest_substring_contains_all_chars(s):
  """We take in a string s and return the length of the shortest 
  substring that contains every unique character in s

  Parameters
  ----------
  s : string
  """
  seen = []
  for char in s:
    if char not in seen:
      seen.append(char)

  print(s[1:])

  return hjalparfall(s, seen)

def hjalparfall(s, seen):
  """We have a list seen and string s and we check in every recursion if 
  we have substring with the tail of s and the beginning og s.
  if the substring exists we recurse with that substring as s
  if it does not exist we return s

  Parameters
  ----------
  s : string
    In every recursion we cut of either the last letter or first.
  seen: list
    List of character. We check if s contains all chars in seen.
  """
  matched_beg = []
  matched_tail = []
  for i in seen:
    matched_beg.append(i in s[:len(s)-1])
  for i in seen:
    matched_tail.append(i in s[1:])

  if (not all(matched_beg) and not all(matched_tail)):
    return len(s)
  if (all(matched_beg)):
    return(hjalparfall(s[:len(s)-1], seen))
  if (all(matched_tail)):
    return(hjalparfall(s[1:], seen))

s = "jiujitsu"
print(shortest_substring_contains_all_chars(s))
def first_recurring_char(str):
  """Returns the first recurring character from a str.

  If str doesn't have any recurring characters it returns None

  Parameters
  ----------
  str : str
  """
  cont = ""
  for i in str:
    if (cont.count(i)) >= 1:
      return i
    cont+= i
  return None

print(first_recurring_char(""))

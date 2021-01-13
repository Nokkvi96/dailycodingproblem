def first_recurring_char(A,m1,m2):
  """We take in matrix A and array m1 and m2 where m1 and m2 represent 
  a place in Array A. 
  
  We find number x in place m1 and find numbers in A smaller than x and set as
  total

  We find number c in place m2 and find numbers in A bigger than c we add c to
  total and return total

  Parameters
  ----------
  A : matrix
    A=NxM matrix where numbers in columns and rows are sorted in ascending order
  m1 : array
    m1=[i,j] where 0 <= i > N and 0 <= j > M
  m2 : array
    m2=[k,l] where 0 <= k > N and 0 <= l > M
  """


a = [[1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]]

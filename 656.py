
import numpy as np

def replace_adjacent_same_color_pixel(A,n,m,c):
  """We take in an array A and a place in the array [n][m]
  we replace every pixel adjacent to n,m that is same color as n,m
  with c. Then we replace A[n][m] with c

  Parameters
  ----------
  A: 2d array
  n: int
    row placement in A
  m: int
    column placement in A
  """
  row,col = A.shape
  original_color = A[n][m]
  for i in range(n-1,n+2):
    if (i < 0 or i >= row):
      break
    else:
      for j in range(m-1,m+2):
        if (j >= 0 and j < col):
          if (A[i][j] == original_color):
            A[i][j] = c
  return A

A= np.array([["B", "B", "W"],
  ["W", "W", "W"],
  ["W", "W", "W"],
  ["B", "B", "B"]])
n,m = 2,2
c = "G"
print(A)
print(replace_adjacent_same_color_pixel(A,n,m,c))


"""
while (innan matrix):
  ## Til hægri 
  if (n+i<col):
    if (A[n+i][m] == original__color):
      A[n+i][m] = c
    ## Diagonal niður
    if (m+i<row and A[n+i][m+i] == original__color):
      A[n+i][m+i] = c
    ## Diagonal upp
    if (m-i>=0 and A[n+i][m-i] == original__color):
      A[n+i][m-i] = c

  ## Til vinstri
  if (n-i>=0):
    if (A[n-i][m] == original__color):
      A[n-i][m] = c
    ## Diagonal niður
    if (m+i<row and A[n-i][m+i] == original__color):
      A[n-i][m+i] = c
    ## Diagonal upp
    if (m-i>=0 and A[n-i][m-i] == original__color):
      A[n-i][m-i] = c

  ## Beint niður
  if (m+i<row and A[n][m+i] == original__color):
    A[n][m+i] == c
  ## Beint upp
  if (m-i>=0 and A[n][m-i] == original__color):
    A[n][m-i] == c
"""

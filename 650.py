import numpy as np

def nr_smaller_m1_bigger_m2(A,m1,m2):
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
  row, col = A.shape

  # If m1 or m2 are not within the boundaries of the places for matrix A
  # We return None
  if ((0>m1[0] or m1[0]>row-1) or (0>m2[0] or m2[0]>row-1) or
      (0>m1[1] or m1[1]>col-1) or (0>m2[1] or m2[1]>col-1)):
    return None
  
  # Transpose of A
  At=np.transpose(A)

  x = A[m1[0],m1[1]]
  c = A[m2[0],m2[1]]
  print(x,c)
  n,m = (m1[0],m1[1])

  # Total number of integers that are not below or to the right of x i.e. integers we know
  # are smaller
  tot=((1+n)*(1+m))-1

  # Iterates over every row above n and adds +1 to tot if j the selcted number is smaller than x
  # If it is not smaller we break and move onto next row
  for i in (range(0,n)):
    for j in (A[i][m+1:]):
      if(j<x):
        tot+=1
      else:
        break

  # Iterates over every column left of m and adds +1 to tot if j the selected number is smaller than x
  # If it is not smaller we break and move onto next column
  for i in (range(0,n)):
    print(tot)
    for j in (At[i][m+1:]):
      if(j<x):
        tot+=1
        print(j)
      else:
        break
  print(tot)

  # (n,m) The place of c in matrix A
  n,m = (m2[0],m2[1])
  # add numbers that are both below and on the rightside of (n,m)
  tot+= ((abs(n-col))*(abs(m-row)))-1

  # Iterates over every row below n and adds +1 to tot if j the selcted number is bigger than c
  # If it is not bigger we break and move onto next row
  for i in range(m, row):
    for j in reversed(A[i][:n]):
      if(j>c):
        tot+=1
      else:
        break

  # Iterates over every column right of m and adds +1 to tot if j the selected number is bigger than c
  # If it is not bigger we break and move onto next column
  for i in range(n, col):
    for j in reversed(At[i][:n]):
      if(j>c):
        tot+=1
      else:
        break
  return tot


A = np.array([[1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45]])


m1 = np.array([1, 1])
m2 = np.array([3, 3])
print(A[1][2])

print(nr_smaller_m1_bigger_m2(A, m1, m2))
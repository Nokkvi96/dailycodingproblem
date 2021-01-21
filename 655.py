def reverse_binary_int(n):
  b= '{0:032b}'.format(n)
  temp = ''
  for i in b:
    print(i)
    if (i == '0'):
      temp+='1'
    else:
      temp+='0'
  return temp

print(reverse_binary_int(10))
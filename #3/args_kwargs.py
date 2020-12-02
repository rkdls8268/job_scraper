def plus(a, b, *args, **kwargs):
  print(args)
  print(kwargs)
  return a+b

plus(1, 2, 3, 1, 1, 1, 1, 1, hello=True, hel=True, dskfh=False)

def plus(*args):
  result = 0
  for num in args:
    result += num
  print(result)

plus(1, 2, 3, 4, 5, 6, 7, 8, 9)
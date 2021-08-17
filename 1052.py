mes = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


mes = read_integer()
if mes == 1:
  print("January")
elif mes == 12:
  print("December")
elif mes == 2:
  print("February")
elif mes == 3:
  print("March")
elif mes == 4:
  print("April")
elif mes == 5:
  print("May")
elif mes == 6:
  print("June")
elif mes == 7:
  print("July")
elif mes == 8:
  print("August")
elif mes == 9:
  print("September")
elif mes == 10:
  print("October")
elif mes == 11:
  print("November")

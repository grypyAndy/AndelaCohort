def find_max_minNum(number):
  minNum = number[0]
  maxNum = number[1]
  if type(number) == list:
    for numbers in number:
      if numbers < minNum:
        minNum = numbers
      elif numbers > maxNum:
        maxNum = numbers
    b = []
    if minNum == maxNum:
      b.append(len(number))
      return b
    else:
      b.append(minNum)
      b.append(maxNum)
      return b
  else:
    return "The input is not a list"
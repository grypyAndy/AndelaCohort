def data_type(y):
  
  #defining some responses needed to return in the if section
  g='no value'
  t='less than 100'
  t1='more than 100'
  t2='equal to 100'
  
  
  #this section tests teh data types provided at input
  if type(y)==type(""):
    return len(y)
  elif type(y)==type([]):
    if len(y)==3:
      return y[2]
    else:
      return None
  elif type(y)==type(2):
    if y < 100:
      return t
    else:
      return t1
    
  elif type(y)==type(None):
    return g
  elif type(y)==type(True):
    return y
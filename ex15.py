class fraction(object):
  def __init__ (self,num,denom):
    self.num=num;
    self.denom=denom;
  def __add__ (self,other):
      return fraction (self.num + other.denom):
  def __sub__ (self,other):
      return fraction (self.num - other.denom):
  def __mult__ (self,other):
      return fraction (self.num * other.denom):
  def __div__ (self,other):
      return fraction (self.num / other.denom):
  def __inv__ (self,other,d):
      d = self.num
      self.num = other.denom
      other.denom = d:
      return fraction (self.num , self.denom)

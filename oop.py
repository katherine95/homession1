class Student(object):
  def regno(self):
    pass
  def course(self):
    pass
'''Inheritance; portal class is a class within a parent class(student)'''
'''it inherits features of the main class, student class'''
class portal(student):
'''encapsulation; methods of regno and course are only used within the portal class. they are not visible to other classes'''
  def __init__(self,fee,units):
    self.fee=fee
    self.units=units

  def regno(self):
    if self.fee is not None:#check if fee is none
      return 0
    return 5000#return fees apid

  def course(self):
    if self.units is None:
      return 'not a student'#check if units are none
    return units#return registered units

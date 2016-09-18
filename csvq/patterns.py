
class Patterns(object):
  def __init__(self):
    self.column = "([a-z]+)"
    self.space = "\s{1}"
    self.float_number = "([0-9]+(?:\.[0-9]+)?)"
    self.string = "'([a-z ]+)'"
    
  def between_pattern(self):
    return (self.column + self.space + "BETWEEN" + 
            self.space + self.float_number + 
            self.space + "AND" + self.space + self.float_number)

  def string_equals_pattern(self):
    return self.column + self.space + "=" + self.space + self.string

  def number_equals_pattern(self):
    return self.column + self.space + "=" + self.space + self.float_number
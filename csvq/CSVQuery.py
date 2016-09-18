import csv, os, re
from patterns import Patterns

class Condition(object):
  def __init__(self, callback, column, args=[]):
    self.__callback = callback
    self.column = column
    self.arguments = args

  def callback(self, arguments=[]):
    args = arguments + self.arguments
    return self.__callback(*args)

class CSVQuery(object):
  def __init__(self, filename="", directory=""):
    self.directory = directory
    self.filename = filename
    self._columns = []
    self._conditions = []

  def __make_columns(self, columns=[]):
    for column in columns.split(","):
      column = self.__clean(column)
      self._columns.append(column)

  def __clean(self, s):
    # Clean up strings.
    s = s.strip()
    return s

  def __str_equals(self, val1, val2):
    return val1 == val2

  def __equals(self, val1, val2):
    return val1 == val2

  def __gt(self, val1, val2):
    return val1 > val2

  def __gte(self, val1, val2):
    return val1 >= val2

  def __lt(self, val1, val2):
    return val1 < val2

  def __lte(self, val1, val2):
    return val1 <= val2

  def __between(self, val0, val1, val2):
    return (val1 < val0) and (val0 < val2)

  def __make_conditions(self, expression=""):
    cond_patterns = {
      "^([a-zA-z]+)\s{1}(=){1}\s{1}'{1}([a-zA-Z]+)'{1}$":  self.__str_equals, 
      "^([a-zA-z]+)\s{1}(=){1}\s{1}([0-9]+(?:\.[0-9]+)?)+$": self.__equals,
      "^([a-zA-z]+)\s{1}(>){1}\s{1}([0-9]+(?:\.[0-9]+)?)+$":  self.__gt,
      "^([a-zA-z]+)\s{1}(<){1}\s{1}([0-9]+(?:\.[0-9]+)?)+$":  self.__lt,
      "^([a-zA-z]+)\s{1}(>=)\s{1}([0-9]+(?:\.[0-9]+)?)+$": self.__gte,
      "^([a-zA-z]+)\s{1}(<=)\s{1}([0-9]+(?:\.[0-9]+)?)+$": self.__lte
    }

    for pattern, callback in cond_patterns.iteritems():
      search = re.search(pattern, expression)
      if search:
        condition = Condition(
            callback=callback,
            column=search.group(1),
            args=[search.group(2)]
          )
        self._conditions.append(condition)

  def SELECT(self, columns=""):
    self.__make_columns(columns)
    return self

  def FROM(self, filename="", directory=""):
    print filename, directory

  def WHERE(self, conditions=""):
    self.conditions = self.__make_conditions(conditions)
    return self

  def BETWEEN(self, column, val1, val2):
    return self

  def LIKE(self, column, val):
    return self

  def AND(self, condition):
    return self

  def OR(self, condition):
    self.__make_conditions(condition)
    return self

  def ORDER_BY(self, columns):
    pass

  def DESC(self):
    pass

  def ASC(self):
    pass

  def SUM(self, column):
    pass

  def AVG(self, column):
    pass

  def get(self):
    result = {}
    if self.directory:
      query_file = self.directory + "/" + self.filename
    
    with open(query_file, 'rb') as infile:
      reader = csv.DictReader(infile)
      for row in reader:
        for condition in self._conditions:
          column = condition.column

          if column in row.keys():
            print type(row[column])
            passes = condition.callback([row[column]])
            if passes:
              print passes

    return result






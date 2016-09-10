import csv, os, re

class Condition(object):
  def __init__(self, callback, column, args=[]):
    self.__callback = callback
    self.column = column
    self.arguments = args

  def callback(self, arguments=[]):
    args = arguments + self.arguments
    return self.__callback(*args)

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


class CSVQuery(object):
  def __init__(self, filename="", directory=""):
    self.directory = directory
    self.filename = filename
    self.columns = []
    self.conditions = []

  def file_fieldnames(self):
    return "... fieldnames from the file selected"

  def __make_columns(self, columns=[]):
    columns_out = []
    for column in columns.split(","):
      column = self.__clean(column)
      columns_out.append(column)
    return columns_out

  def __clean(self, s):
    s = s.strip()
    return s

  def __make_conditions(self, conditions=""):
    # find all in parens
    pattern = "\(([^\)]+)\)"
    expressions = re.findall(pattern, conditions)
    operators = re.sub(pattern, "", conditions)
    print expressions, operators.split()

    patterns = Patterns()
    # between
    pattern = re.compile(patterns.between_pattern(), re.IGNORECASE)
    groups = pattern.findall(conditions)
    for group in groups:
      self.conditions.append(
        Condition(
          callback=self.__between, 
          column=group[0], 
          args=[float(group[1]), float(group[2])]
        )
      )

      # equals for strings
      pattern = re.compile(patterns.string_equals_pattern(), re.IGNORECASE)
      groups = pattern.findall(conditions)
      for group in groups:
        self.conditions.append(
          Condition(
            callback=self.__equals,
            column=group[0],
            args=[group[1]]
          )
        )

        print self.conditions[1].callback(["New York"])

  def select(self, columns=""):
    self.columns = self.__make_columns(columns)
    # if self.columns and self.conditions:
    #   return self.run()
    return self

  def where(self, conditions=""):
    self.conditions = self.__make_conditions(conditions)
    # if self.columns and self.conditions:
    #   return self.__run()
    # return self

  def __equals(self, val1, val2):
    return val1 == val2

  def __gt(self, val1, val2):
    return val1 > val2

  def __between(self, val0, val1, val2):
    return (val1 < val0) and (val0 < val2)

  def __run(self):
    result = {}
    if self.directory:
      query_file = self.directory + "/" + self.filename
    with open(query_file, 'rb') as infile:
      reader = csv.DictReader(infile)
      for row in reader:
        for condition in self.conditions:
          if row["name"].strip() == "New York":
            result["name"] = row["name"]
            result["pop"] = row["pop"]


      return result






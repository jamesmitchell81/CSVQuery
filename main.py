from csvq import CSVQuery

def main():

  query = CSVQuery(filename="2014_us_cities.csv", directory="./datasets")

  # query.SELECT("name, pop")
  # query.FROM(directory="./datasets")
  # query.WHERE("name = 'New York'")
  # query.AND("")
  # query.OR("name = 'James'")
  # query.LIKE("name", "Zoo York")
  # query.BETWEEN("pop", 1000000, 3000000)
  # query.ORDER_BY("pop").ASC()
  # query.ORDER_BY("pop").DESC()

  # query.SUM("pop").WHERE("this = 'that'")
  # query.AVG("pop").WHERE("this = 'that'")

  query.SELECT("name, pop").WHERE("pop > 1000000")

  result = query.get()
  
  print query._columns
  print query._conditions

if __name__ == "__main__":
  main()
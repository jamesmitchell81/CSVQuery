from CSVQuery import CSVQuery

def main():

  query = CSVQuery(filename="2014_us_cities.csv", directory="./datasets")

  query.SELECT("name, pop")
  query.FROM(directory="./datasets")
  query.WHERE("name = 'New York'")
  query.AND("")
  query.OR("name = 'James'")
  query.LIKE("name", "Zoo York")
  query.BETWEEN("pop", 1000000, 3000000)
  query.ORDER_BY("pop").ASC()
  query.ORDER_BY("pop").DESC()

  query.SELECT("name").WHERE("name = 'James'").OR("pop > 1,0000,00")

  query.SUM("pop")
  query.AVG("pop")
  

if __name__ == "__main__":
  main()
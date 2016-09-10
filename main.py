from CSVQuery import CSVQuery

def main():

  query = CSVQuery(filename="2014_us_cities.csv", directory="./datasets")

  # result = csv.select(["name", "pop"]).equals({"name":"New York"}).gt({'pop':3000000})
  # result = csv.select("name, pop").where("name = 'New York' OR pop > 3000000")
  query.select("name, pop")
  query.where("(name = 'New York') and (pop > 1000000 and pop < 2000000) or (name = 'James')")

if __name__ == "__main__":
  main()
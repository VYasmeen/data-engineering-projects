import csv

def read_csv(file_path):
  records = []

  with open(file_path, mode="r", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      for row in reader:
          records.append(row)
  return records

if __name__ == "__main__":
    data = read_csv("data/ecommerce_sales.csv")
    print("Total records:", len(data))
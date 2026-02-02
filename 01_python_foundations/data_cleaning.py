from data_ingestion import read_csv

class DataCleaner:
    def __init__(self.records):
        self.records=records

def clean(self):
    cleaned_records =[]

    for row in records:
        if row:
            cleaned_records.append(row)
    return cleaned_records

if __name__=="__main__":
    data=read_csv("data/ecommerce_sales.csv")
    cleaner=DataCleaner(data)
    cleaned=cleaner.clean()
    print("Cleaned records:",len(cleaned))
    

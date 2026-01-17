from data_ingestion import read_csv

def clean_data(records):
    cleaned_records =[]

    for row in records:
        if row:
            cleaned_records.append(row)
    return cleaned_records

if __name__=="__main__":
    data=read_csv("data/ecommerce_sales.csv")
    cleaned=clean_data(data)
    print("Cleaned records:",len(cleaned))
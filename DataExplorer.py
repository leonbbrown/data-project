# headers == index

import csv
import pandas as pd

csv_path = 'C:\\Users\\leon8\\OneDrive\\Desktop\\Workspace\\VS Code Projects\\data-project\\sales_data.csv'
csvreader = csv.reader(csv_path)
name = {}

df = pd.read_csv(csv_path)
customer_name_column = df['Customer Name']

def check_order_amount():
    for i in customer_name_column:
        if i in name:
            name[i] += 1
        else:
            name[i] = 1
    print('Customer + order amount is as follows:')
    print(name)
    

    
    

check_order_amount()

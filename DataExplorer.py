# headers == index

import csv
import pandas as pd

csv_path = 'C:\\Users\\leon8\\OneDrive\\Desktop\\Workspace\\VS Code Projects\\data-project\\sales_data.csv'
csvreader = csv.reader(csv_path)
name = {}
df = pd.read_csv(csv_path)
customer_name_column = df['Customer Name']
payment_method_column = df['Payment Method']
sku_column = df['Product SKU']


def check_order_amount():
    for i in customer_name_column:
        if i in name:
            name[i] += 1
        else:
            name[i] = 1
    print('Customer + order amount is as follows:')
    print(name)
    

def check_payment():
    most_popular_payment = payment_method_column.mode()
    print('The payment method users prefer most is:')
    if most_popular_payment.values == 'Debit':
        print('Debit')
    elif most_popular_payment.values == 'Credit':
        print('Credit')
    else:
        print('PayPal')
   
def check_sku():
    sku_map = {
    174832: 'jeans',
    126594: 'T- shirt',
    198765: 'Hoodie',
    142307: 'Knitted Sweater',
    186905: 'Socks',
    195472: 'Boxer Breifs'
        
}
    
    most_popular_sku = sku_column.mode().values
    sku_list = most_popular_sku.tolist()
    print('These are the most popular products:')
    new_list = [sku_map[k] for k in sku_list]
    print(new_list)


check_sku()


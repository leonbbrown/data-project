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
    most_popular_sku = sku_column.mode().values
    print('These are the most popular products:')
    print(most_popular_sku)
    
    #print('the most popular product is:')
    #if most_popular_sku == '174832':
        #print('Jeans')
    #elif most_popular_sku == '126594':
        #print('T-shirt')
    #elif most_popular_sku == '198765':
        #print('Hoodie')
    #elif most_popular_sku == '142307':
        #print('Knitted Sweater')
    #elif most_popular_sku == '186905':
        #print('Socks')
    #else: #195472
        #print('Boxer Breifs')

check_sku()

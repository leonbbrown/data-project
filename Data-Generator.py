import csv
import pandas as pd
import random


customer_name = []
prod_sku = []
quantity = []
payment = []
dates = []

#👇 paste own path to sales_data.csv

filepath = 'C:\\Users\\leon8\\OneDrive\\Desktop\\Workspace\\VS Code Projects\\data-project\\sales_data.csv'

while True:
    row_count = input('How many rows would you like? ')

    if not row_count.isdigit():
        print('Please enter a valid number!')
    else:
        rows = int(row_count)
        
        
        break 

#generates random dates
def gen_date(rows, dates):
    for _ in range(rows):
        month = random.randint(1, 4)
        day = random.randint(1, 28)
        date = f'{day}/{month}/24'
        dates.append(date)
    return dates

#generates random quantity
def get_quantity(rows, quantity):
    for _ in range(rows):
        random_quantity = random.randint(1,6)
        quantity.append(random_quantity)
    return quantity


#appends a random SKU to a customers row
def get_sku(rows, prod_sku):
    sku = [174832, 126594, 198765, 142307, 186905, 195472]
    for _ in range(rows):
        number = random.choice(sku)
        prod_sku.append(number)
    return prod_sku

#fetches random name from customer pool
def get_name(rows,customer_name):
    random_names = ['Timothy Lawson', 'Jackson Barnes', 'Archer Palmer', 'Francis Thomson', 'Patrick Kennedy', 'Stella Pearson']
    for _ in range(rows):
        name = random.choice(random_names)
        customer_name.append(name)
    return customer_name

#selects a random payment method for each row
def get_payment_method(rows, payment):
    payment_method = ['Credit', 'Debit', 'Paypal']
    for _ in range(rows):
        method = random.choice(payment_method)
        payment.append(method)
    return payment

#executes all above functions
def gen():
    gen_date(rows, dates)
    get_quantity(rows, quantity)
    get_sku(rows, prod_sku)
    get_name(rows,customer_name)
    get_payment_method(rows, payment)

#calls the function 
gen()

#Stores generated data in dictionary
dict = {
    'Date': dates,
    'Customer Name': customer_name,
    'Product SKU': prod_sku,
    'Quantity': quantity,
    'Payment Method': payment
}   

#adds data to the csv file
df = pd.DataFrame(dict)
df.to_csv(filepath, index=False)
print('Successfully added data to sales_data.csv!')



   
    



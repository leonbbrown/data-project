import csv
import pandas as pd
import random
import matplotlib.pyplot as plt



customer_name = []
prod_sku = []
quantity = []
payment = []
dates = []

#👇 paste own path to sales_data.csv

csv_path = 'C:\\Users\\leon8\\OneDrive\\Desktop\\Workspace\\VS Code Projects\\DATA\\sales_data.csv'

while True:
    print(
        '''
________       _____            _________                              _____              
___  __ \_____ __  /______ _    __  ____/_____________________________ __  /______________
__  / / /  __ `/  __/  __ `/    _  / __ _  _ \_  __ \  _ \_  ___/  __ `/  __/  __ \_  ___/
_  /_/ // /_/ // /_ / /_/ /     / /_/ / /  __/  / / /  __/  /   / /_/ // /_ / /_/ /  /    
/_____/ \__,_/ \__/ \__,_/      \____/  \___//_/ /_/\___//_/    \__,_/ \__/ \____//_/     
                                                                                                                    
Welcome to Simulated-Sales-Analyzer!

To get started let's generate some data.
                                       
'''
    )
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
df.to_csv(csv_path, index=False)
print('Successfully added data to sales_data.csv!')

#DATA EXPLORER
name = {}
try:
    df = pd.read_csv(csv_path)
    # checks if df/csv is empty
    if df.empty:
        print('CSV file is empty! please run Data-Generator.py')
    else:
        customer_name_column = df['Customer Name']
        payment_method_column = df['Payment Method']
        sku_column = df['Product SKU']
        #checks how many orders each user placed
        def check_order_amount():
            for i in customer_name_column:
                if i in name:
                    name[i] += 1
                else:
                    name[i] = 1
            print('Customer + order amount is as follows:')
            print(name)

        def check_payment():
            # finds most popular payment method + prints it as a string
            most_popular_payment = payment_method_column.mode()
            print('The payment method users prefer most is:')
            if 'Debit' in most_popular_payment.values:
                print('Debit')
            elif 'Credit' in most_popular_payment.values:
                print('Credit')
            elif 'PayPal' in most_popular_payment.values:
                print('PayPal')
            else:
                print('please dont alter the file manually!')

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
            # replaces SKU with actual item the SKU represents
            new_list = [sku_map[k] for k in sku_list]
            print(new_list)

        def customer_purchase():
            #group customer name column + quantity 
            customer_purchases = df.groupby('Customer Name')['Quantity'].sum().reset_index()
            #adds all purchases for each customer and shows from most purchased to least
            customer_purchases_sorted = customer_purchases.sort_values(by='Quantity', ascending=False)
            print(customer_purchases_sorted)

            #plot the values of each customer
            plt.figure(figsize=(10, 6))
            plt.bar(customer_purchases_sorted['Customer Name'], customer_purchases_sorted['Quantity'], color='#FFA500')
            plt.xlabel('Customer Name')
            plt.ylabel('Quantity Purchased')
            plt.title('Quantity of Purchases by Customer')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

        def show_data():
            if df.empty:
                print('CSV file is empty! please run Data-Generator.py')
                return
            print(
                '''
________       _____            __________              ______                         
___  __ \_____ __  /______ _    ___  ____/___  ____________  /_________________________
__  / / /  __ `/  __/  __ `/    __  __/  __  |/_/__  __ \_  /_  __ \_  ___/  _ \_  ___/
_  /_/ // /_/ // /_ / /_/ /     _  /___  __>  < __  /_/ /  / / /_/ /  /   /  __/  /    
/_____/ \__,_/ \__/ \__,_/      /_____/  /_/|_| _  .___//_/  \____//_/    \___//_/     
                                                /_/                                    
                '''
            )
            check_order_amount()
            print()
            check_payment()
            print()
            check_sku()
            print()
            customer_purchase()
            print()

# calls function to execute the visualizer

        show_data()
# common errors + solution
except pd.errors.EmptyDataError:
    print('EmptyDataError: CSV file is empty! please run Data-Generator.py')
except FileNotFoundError:
    print('FileNotFoundError: Please create a blank CSV File and update the file paths in DataExplorer.py and Data-Generator.py')
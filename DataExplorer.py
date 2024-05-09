import csv
import pandas as pd
import matplotlib.pyplot as plt

#👇 paste own path to sales_data.csv

csv_path = 'C:\\Users\\leon8\\OneDrive\\Desktop\\Workspace\\VS Code Projects\\data-project\\sales_data.csv'
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
 _____         _                 
|   __|_ _ ___| |___ ___ ___ ___ 
|   __|_'_| . | | . |  _| -_|  _|
|_____|_,_|  _|_|___|_| |___|_|  
          |_|                    
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
import numpy as np
import pandas as pd

m = int(input("Enter maximum capacity: "))
n = int(input("Enter review period: "))
d = int(input("Enter number of simulation days: "))
x = int(d/n)
begining_inventory = int(input("Enter begining inventory: "))
demand = 0
ending_inventory = 0
shortage_quantity = 0
order_quantity = 8
days_of_shortage = 0
days_until_order_arrives = 2
ending_inventory_list = []
days = []
Day = []
Begining_Inventory = []
Demand = []
Ending_Inventory = []
Shortage = []
Order = []
Lead_Time = []

for cycle in range(1, x+1):

    for day in range(1, n+1):
        Day.append(day)
        days_until_order_arrives = days_until_order_arrives-1

        if days_until_order_arrives == -1:
            begining_inventory = ending_inventory+order_quantity

        daily_demand = np.random.choice(
            a=[0, 1, 2, 3, 4], p=[0.10, 0.25, 0.35, 0.21, 0.09])
        total_demand = daily_demand + shortage_quantity
        if total_demand > begining_inventory:
            shortage_quantity = total_demand-begining_inventory
            ending_inventory = 0
            if shortage_quantity > 0:
                days_of_shortage = days_of_shortage+1
        else:
            ending_inventory = begining_inventory-total_demand
            shortage_quantity = 0
        ending_inventory_list.append(ending_inventory)

        Begining_Inventory.append(begining_inventory)
        Demand.append(daily_demand)
        Ending_Inventory.append(ending_inventory)
        Shortage.append(shortage_quantity)

        begining_inventory = ending_inventory

        if day == n:

            days_until_order_arrives = np.random.choice(
                a=[1, 2, 3], p=[0.6, 0.3, 0.1])
            order_quantity = m-ending_inventory+shortage_quantity
            Order.append(order_quantity)
        if day != n:
            Order.append("-")
        if days_until_order_arrives >= 0:
            Lead_Time.append(days_until_order_arrives)
        else:
            Lead_Time.append("-")

        data = pd.DataFrame(list(zip(Day, Begining_Inventory, Demand, Ending_Inventory, Shortage, Order, Lead_Time)),
                            columns=['Day', 'Begining_Inventory', 'Demand', 'Ending_Inventory', 'Shortage', 'Order', 'Lead_Time'])
print(data)


total = sum(ending_inventory_list)
average_ending_inventory = total/d
print("Average Ending Inventory =", average_ending_inventory)

average_shortage_days = days_of_shortage/d
print("Average Shortage Days", average_shortage_days)

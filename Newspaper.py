import pandas as pd
import random

n = int(input("Enter Number of Newspapers"))
d = int(input("Enter Number of Days"))
typeRN = 0
type = 0
dmdRN = 0
dmd = 0
revenue = 0
lp = 0
srp = 0
cost = round((0.33 * n), 2)
Cost = []
for i in range(1, d+1):
    Cost.append(str(cost))
p = 0
RN_TON = []
TON = []
RN_dmd = []
demand = []
rev = []
lost = []
scrap = []
profit = []
day = [i for i in range(1, d+1)]

for i in range(d):
    typeRN = random.randint(1, 100)
    RN_TON.append(typeRN)
    if typeRN < 36:
        type = "good"
    elif typeRN < 81:
        type = "fair"
    elif typeRN < 101:
        type = "poor"
    TON.append(type)
    dmdRN = random.randint(1, 100)
    RN_dmd.append(dmdRN)
    if type == "poor" and dmdRN < 45:
        dmd = 40
    elif type == "poor" and dmdRN < 67:
        dmd = 50
    elif type == "poor" and dmdRN < 83:
        dmd = 60
    elif type == "poor" and dmdRN < 95:
        dmd = 70
    elif type == "poor" and dmdRN < 101:
        dmd = 80
    elif type == "fair" and dmdRN < 11:
        dmd = 40
    elif type == "fair" and dmdRN < 29:
        dmd = 50
    elif type == "fair" and dmdRN < 69:
        dmd = 60
    elif type == "fair" and dmdRN < 89:
        dmd = 70
    elif type == "fair" and dmdRN < 97:
        dmd = 80
    elif type == "fair" and dmdRN < 101:
        dmd = 90
    elif type == "good" and dmdRN < 4:
        dmd = 40
    elif type == "good" and dmdRN < 9:
        dmd = 50
    elif type == "good" and dmdRN < 24:
        dmd = 60
    elif type == "good" and dmdRN < 44:
        dmd = 70
    elif type == "good" and dmdRN < 79:
        dmd = 80
    elif type == "good" and dmdRN < 94:
        dmd = 90
    elif type == "good" and dmdRN < 101:
        dmd = 100
    else:
        dmd = 0
    demand.append(dmd)
    revenue = dmd * 0.5
    rev.append(str(revenue))
    if dmd > n:
        lp = (dmd - n) * 0.17
    else:
        lp = 0
    lost.append(str(round(lp, 2)))

    if dmd < n:
        srp = (n - dmd) * 0.05
    else:
        srp = 0
    scrap.append(str(srp))

    p = revenue - cost - lp + srp
    profit.append(str(round(p, 2)))


data = pd.DataFrame(list(zip(day, RN_TON, TON, RN_dmd, demand, rev, Cost, lost, scrap, profit)),
                    columns=['Day', 'RN for TON ', 'TON', 'RN for Demand', 'Demand', 'Sales Revenue', 'NPs cost', 'Lost Profit', 'Scrap', 'Daily Profit'])

print(data)

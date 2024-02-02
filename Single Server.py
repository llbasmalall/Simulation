import pandas as pd
import random
customerNumber = int(input("Welcome to Our Single Server Queue Simulation System please Enter Number of Customers"))
server = 1

IAT = []
for i in range(0, customerNumber):
    r = random.randint(1, 8)
    IAT.append(r)
serviceTimes = []
for i in range(0, customerNumber):
    n = random.randint(1, 6)
    serviceTimes.append(n)

arrivalTimes = []
endTimes = []

arrivalTimes = [0 for i in range(customerNumber)]
endTimes = [0 for i in range(customerNumber)]

arrivalTimes[0] = IAT[0]

for i in range(1, customerNumber):
    arrivalTimes[i] = (arrivalTimes[i-1] + IAT[i])

endTimes[0] = arrivalTimes[0]+serviceTimes[0]
for i in range(1, customerNumber):
    lastEnd = endTimes[:i]
    lastEnd.sort(reverse=True)
    lastEnd = lastEnd[:server]
    if i < server:
        endTimes[i] = arrivalTimes[i] + serviceTimes[i]
    else:
        endTimes[i] = (max(arrivalTimes[i], min(lastEnd)) + serviceTimes[i])

totalTimes = [((endTimes[i]-arrivalTimes[i]))
              for i in range(customerNumber)]
waitTimes = [(totalTimes[i] - serviceTimes[i])
             for i in range(customerNumber)]

data = pd.DataFrame(list(zip(IAT, arrivalTimes, serviceTimes, endTimes, waitTimes, totalTimes)),
                    columns=['Inter-arrival Time', 'Arrival Time', 'Service Time', 'End Time', 'Waiting Times', 'Total Time in System'])

print(data)


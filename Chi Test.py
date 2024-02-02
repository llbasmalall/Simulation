import random
import scipy
alpha = float(input("Enter Alpha"))
RN = []
n = int(input("Enter Number of Random Numbers"))
choose = int(input(
    "Enter 1 if you want the computer to generate your Random Numbers. Enter 2 if you want to Enter your Random Numbers"))
if choose == 1:
    for i in range(0, n):
        RN.append(i)
        RN[i] = random.randint(1, 100)
elif choose == 2:
    for i in range(0, n):
        RN.append(i)
        RN[i] = input()
print(RN)

O1 = 0
O2 = 0
O3 = 0
O4 = 0
O5 = 0
O6 = 0
O7 = 0
O8 = 0
O9 = 0
O10 = 0
for i in RN:
    if i in range(1, 11):
        O1 += 1
    if i in range(11, 21):
        O2 += 1
    if i in range(21, 31):
        O3 += 1
    if i in range(31, 41):
        O4 += 1
    if i in range(41, 51):
        O5 += 1
    if i in range(51, 61):
        O6 += 1
    if i in range(61, 71):
        O7 += 1
    if i in range(71, 81):
        O8 += 1
    if i in range(81, 91):
        O9 += 1
    if i in range(91, 101):
        O10 += 1

Ei = n//10

X1 = (pow((O1-Ei), 2)) / Ei
X2 = (pow((O2-Ei), 2)) / Ei
X3 = (pow((O3-Ei), 2)) / Ei
X4 = (pow((O4-Ei), 2)) / Ei
X5 = (pow((O5-Ei), 2)) / Ei
X6 = (pow((O6-Ei), 2)) / Ei
X7 = (pow((O7-Ei), 2)) / Ei
X8 = (pow((O8-Ei), 2)) / Ei
X9 = (pow((O9-Ei), 2)) / Ei
X10 = (pow((O10-Ei), 2)) / Ei

Chi_Square = int(X1+X2+X3+X4+X5+X6+X7+X8+X9+X10)
print("Chi-Square value is", Chi_Square)
Critical_Value = scipy.stats.chi2.ppf(1-alpha, 10-1)
print("Critical Value is", Critical_Value)
if Chi_Square < Critical_Value:
    print("H0 is not rejected")
else:
    print("H0 is rejected")

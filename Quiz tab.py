# Take input from user if user input a number greater than 100 print congratulations you input a nunber greater than 100 !
# while (True):
#     x=int(input("Enter a number: "))
#     if x<=100:
#         print("The number you enter is not greater than 100. Enter Again.")
#         continue
#     else:
#         print("Congratulations you input a number greater than 100 which is",x)
#     break
# Press ctrl+/ to comment out.
# To print the docstring of function type print(func.__doc__)
# x = ['PH-121', 'HS-101', 'CY-105', 'HS-105/12', 'MT-111', 'CS-105', 'CS-106', 'EL-102','EE-119', 'ME-107', 'CS-107', 'CGPA']
# print(x)
# j = 0
# y = []
#
# for i in range(len(x)):
#     a = float(input(f"Enter Marks of {x[j]}:"))
#     y.append(a)
#     j=j+1
#     if j > len(x):
#         break
#
# y = [y]
# print(y)


# Equation
def dydx(x, y):
    return (((1.13 - 1) / (49 + 1.13)) * x * y)


# RK Method Exact
def rungeKuttaExact(x0, y0, x, h):
    n = (int)((x - x0) / h)  # Counting number of intervals
    y = y0
    exact = []
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * dydx(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * dydx(x0 + h, y + k3)
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)  # Updating next value of y
        exact.append(y)
        x0 = x0 + h  # Updating next value of x
    print("Number of intervals at", h, "are", i)
    return exact


# RK Method Approx
def rungeKuttaApprox(x0, y0, x, h, C1, C2, C3, C4, Theta1, Theta2, Theta3, W1, W2, W3):
    n = (int)((x - x0) / h)  # Counting number of intervals
    y = y0
    approx = []
    for i in range(1, n + 1):
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dydx(x0, y)
        k2 = h * dydx(x0 + Theta1 * h, y + W1 * k1)
        k3 = h * dydx(x0 + Theta2 * h, y + W2 * k2)
        k4 = h * dydx(x0 + Theta3 * h, y + W3 * k2)
        y = y + (C1 * k1 + C2 * k2 + C3 * k3 + C4 * k4)  # Update next value of y
        approx.append(y)
        x0 = x0 + h  # Update next value of x
    return approx


# Root Mean Square
def RMS(exactList, approxList, x, x0, h):
    n = (int)((x - x0) / h)
    sum = 0
    for i in range(0, n):
        difference = approxList[i] - exactList[i]
        differenceSquare = difference ** 2
        sum = sum + differenceSquare
    division = sum / n
    root_mean_square_error = division ** (0.5)
    return root_mean_square_error


h = (((49 * 1.13) / (49 + 1.13)) / 7)
Width_Of_Interval = [h, h / 2, h / 4, h / 8, h/ 16]

for h in Width_Of_Interval:
    x0 = 0
    y = ((1.13 - 1) / 1.13)
    x = ((49 * 1.13) / (49 + 1.13))
    C1 = 1 / 8
    C2 = 0.30
    C3 = 0.45
    C4 = 1 / 8
    Theta1 = 0.25
    Theta2 = 0.75
    Theta3 = 1
    W1 = 0.25
    W2 = 0.75
    W3 = 1
    exact_values = rungeKuttaExact(x0, y, x, h)
    print("exact values at ", h, "widh of interval =", exact_values)
    approx_values = rungeKuttaApprox(x0, y, x, h, C1, C2, C3, C4, Theta1, Theta2, Theta3, W1, W2, W3)
    print("approx values at ", h, "widh of interval =", approx_values)
    rms_error = RMS(exact_values, approx_values, x, x0, h)
    print("RMS at", h, "(width of interval) is", rms_error)
    print("")




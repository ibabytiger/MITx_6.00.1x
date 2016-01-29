# set baseline figures
balance = 320000
annualInterestRate = 0.2
epsilon = 0.01

monthlyInterestRate = annualInterestRate / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0
payment = (upperBound + lowerBound) / 2.0
remainingBalance = balance

while abs(remainingBalance) >= epsilon: # <- this is the problem
    remainingBalance = balance # reset the balance
    for n in range(1, 13):
        unpaidBalance = remainingBalance - payment
        interest = unpaidBalance * monthlyInterestRate
        remainingBalance = unpaidBalance + interest
    #print "Upper: " + str(upperBound)
    #print "Lower: " + str(lowerBound)
    #print "Payment: " + str(payment)
    #print "Remaining Balance: " + str(remainingBalance)

    if remainingBalance < 0:
        upperBound = payment
    else:
        lowerBound = payment
    payment = (upperBound + lowerBound) / 2.0
print "Lowest Payment: " + str(round(payment,2))

balance = 3329
newBalance = balance
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
months = 12
paymentAmount = 0

while newBalance >= 0:
    paymentAmount += 10 # increment payment amount
    newBalance = balance # reset the balance

    for n in range(1, 13):
        unpaidBalance = newBalance - paymentAmount # make month payment
        interest = unpaidBalance * monthlyInterestRate # accrue interest
        newBalance =  unpaidBalance + interest # update new balance
        #print "Month " + str(n) +" Balance: " + str(newBalance)
    #print "New Payment Amount: " + str(paymentAmount)
print "Lowest Payment: " + str(paymentAmount)

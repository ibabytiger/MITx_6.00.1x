balance = 4213
newBalance = balance
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12
months = 12
totalPaid = 0

for n in range (1, 13):
    print "Month: " + str(n)
    minPayment = round(newBalance * monthlyPaymentRate, 2)
    totalPaid += minPayment
    print "Minimum monthly payment: " + str(minPayment)

    unpaidBalance = newBalance - minPayment
    interest = monthlyInterestRate * unpaidBalance
    newBalance = round((unpaidBalance + interest), 2)
    print "Remaining balance: " + str(newBalance)

print "Total paid: " + str(totalPaid)
print "Remaining balance: " + str(newBalance)

print('WELCOME')
balance = 25000
accountnumber = input('Enter Account Number:')
password = input('Enter Password:')
if accountnumber =='6080987215' and password == 'hasan@098':
    print('Welcome Hasan')
else:
    print('Wrong Account Number Or Password')
withdrawal = int(input('Enter the amount to withdrawal ='))
if withdrawal ==100:
    print('Balance amount =',balance-withdrawal)
elif withdrawal ==500:
    print('Balance amount =', balance - withdrawal)
elif withdrawal ==2000:
    print('Balance amount =', balance - withdrawal)
else:
    print('SORRY Only 100,500,2000 Cash Notes are avaliable')
print('Thank you')
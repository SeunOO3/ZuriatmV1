name = input('what is your name? \n')
allowedUsers = ['Seun', 'Iyin', 'Tobi', 'Amara']
allowedPassword = ['passwordSeun', 'passwordIyin', 'passwordTobi', 'passwordAmara']

if(name in allowedUsers):
    password = input('what is your password? \n')
    UserId = allowedUsers.index(name)

    if password == allowedPassword[UserId]:
        print('Welcome %s' %name)
       
        import datetime
        e = datetime.datetime.now()
        
        print ("Today's date:  = %s/%s/%s" % (e.day, e.month, e.year))
        print ("The time is now: = %s:%s:%s" % (e.hour, e.minute, e.second))
        print('These are the available options')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        if selectedOption == 1:
            print('you selected %s' % selectedOption)
            accountBalance = 100000
            amount = int(input ('How much will you like to withdraw? \n'))
            if amount <  accountBalance:
                 print('Please take your cash, Would you like to continue with another option')
            elif amount > accountBalance:
                print('Insufficient balance, please try later')
                print('1. Yes')
                print('2. No')
            selectOption = int(input('Please select an option:'))
            if selectOption == 1:
                print('please enter password')
            elif selectOption == 2:
                print('please take your card')

        elif selectedOption == 2:
            print('you selected %s' % selectedOption)
            accountBalance = 100000
            deposit = int(input ('How much will you like to deposit? \n'))
            accountBalance = accountBalance + deposit
            print('Deposit successful, Your current balance is %s' % accountBalance)
       
       
        elif selectedOption == 3:
            print('you selected %s' % selectedOption)
            Inbox = input('Please enter your complaint.. \n')
            print('Complaint received. Thank you for contacting us.')
        else:
            print('Invalid Option selected, please try again')


    else:
        print('Password incorrect, please try again')

else:
    print('Name not found, please try again')


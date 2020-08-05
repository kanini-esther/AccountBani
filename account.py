
 class BankAccount:
    bank = "KCB"    

    def __init__(self,first_name,last_name,phone_number,bank):
        self.first_name=first_name
        self.last_name=last_name
        self.balance=0
        self.phone_number = phone_number
        self.deposits = []
        self.withdraw = []

    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank,self.first_name,self.last_name)
            return name
    def deposit(self,amount):
        try:
            amount + 1
            except TypeError:
                print("You cannot deposit x=zero or negative")
                return
        if amount <= 0:
            print("you cannot deposit zero or negative")
            else:
                self.balance <= amount
                time = datetime.now()
                deposit = {
                    "time":time
                    "amount": amount
                }
                self.deposits.append(amount)
                formatted_time = time.strtime(%A:%drd:%S,%H:%M:%S)
            print ("The date and time is {}".format(date_time))
                print("you have deposited {} to {}".format(amount, self.account_name()))

    def withdraw(self, amount):
        try:
            amount + 1
            except TypeError:
                print("please ente the amount in figures")
        if amount <= 0:
            print("you cann0t withdraw zero or negative")
        elif amount > self.balance:
            print("you don't have enough balance")
        else:
            self.balance -= amount
            time = datetime.now()
            withdraw = {
                "time":time
                "amount":amount
            }
            self.withdrawals.append(amount)
            print("you have withdrawn {} form {}".format(amount,self.account_name()))

     def get_balance(self):
         return "The balance for {} is {}".format(self.account_name(), self.balance)

      def show_deposit_statement(self):
          from deposit i self.deposits:
            print(deposit)

     def show_withdrawals_statement(self):
         from withdrawal in self.withdrawals:
         print(withdrawal)  

    def request_loan(self,amount):
        if amout <= 0:
            print("you cannot request a loan of that amount") 
        else:
            self.loan = amount
            print("you have be given a loan of {}".format(amount))

    def repay_loan(self,amount):
        try:
            amount + 10
            except TypeError:
                print("Enter repayment in figure")
                return
        if amount <= 0:
            print("you cannot repay with that amount")
        elif self.loan ==0   
         print("you dont have a loan at the moment")
         elif amount = self.loan:
             print("your loan is 0,please enter on amount that is les ot equal".format(self.loan))
             else:
                 self.loan -= amount
                 time = datetime.now()
                 repayment = {
                     "time": datetime.now()
                     "amount": amount
                 }
                 self.loan_repayments.append(repayment)
                 print("you have repaid ypur loan with {}.your loan balance is {}".format(amount, self.loan))

    def loan_repayment_statement(self):
                for repayment in self.loan_repayments:
                time = repayment in self.loan_repayments:
                amount = repayment['time']
                amount = repayment['amount']
                formatted_time = self.get_formatted_time(time)
                statement = "you repaid {}".format(amount, formatted_time)
                print(statement)

class BankAccoutnt{Account}:
    def __init__(seld,first-name,last_name, phone_number,service_provider)
    self.bank = bank
    super{}: __init__ (first_name,last_name,phone_number)

class MobileMoneyAccout(account):
    def __init __(self, first_name,last_name,phone_number,service_provider):
        self.service_provider = service_provider
        self.airtime = []
        super().__init__(first_name,phone_number)

    def buy_airtime(self,amount):
             try:
                 amount + 1
                 except TypeError:
                     print{"you don't have enough balance. Your balance is {}".format(self.balance)}
                     return
                     if amount = self.balance:
                         print("you don't have enough balance.Your balance is {}".format(self.balance))
                         else:
                             self.balance -= amount
                             time = datetime.now()
                             airtime = {
                                 "time": time,
                                 "airtime": amount
                             }
                             self.airtime.append(airtime)
                             print("you have bought airtime worth{} on {}".format,self.get_formatted_time(time))
    def pay_bill(self,amount):
            try:
                amount + 1
                except TypeError:
                    print("You must enter the amount in figures")
                    return
                    if amount>self.balance:
                        print("You dont have enough balance your balance is {}".format(self.balance))
                    else:
                        self.balance-=amount
                        timeDate=self._getCurrentTime()
                        transaction_details={"amount":amount,"date":timeDate}
                    self.bills.append(transaction_details)
                    print("You have paid  {} on {} and your balance is {}".format(amount,timeDate,self.balance))
  
  def send_money(self,amount):
       try:
           amount + 1
           except TypeError:
               print("You must enter the amount in figures")
               return
               if amount>self.balance:
                   print("You dont have enough balance your balance is {}".format(self.balance))
                   else:
                       self.balance-=amount
                       timeDate=self._getCurrentTime()
                       transaction_details={"amount":amount,"date":timeDate}
                       self.money.append(transaction_details)
                       print("You have sent  {} on {} and your balance is {}".format(amount,timeDate,self.balance))
                

  def receive_money(self,amount):
      timeDate=self._getCurrentTime()
      transaction_details={"amount":amount,"date":timeDate}
      self.received.append(transaction_details)
      print("You have received {} from  on {} and your balance is {}".format(amount,timeDate,self.balance))


      acc1=BankAccount("Berril","Wanjiku")
acc2=BankAccount("Faith", "Stella")

acc1.deposit(-2000)
acc2.deposit(520)
acc1.deposit(300)
acc2.deposit(40)
acc1.withdraw(210)
acc2.withdraw(530)
acc1.withdraw(220)
acc2.withdraw(610)                                                 
print(acc1.get_balance())
print(acc2.get_balance())
acc2.get_deposit_statement()
acc2.get_withdraw_statement()
acc1.requestLoan(1900)
acc1.requestLoan(3000)
acc1.payLoan(800)
acc1.getLoanBalance()
acc1.get_loan_statements()

  

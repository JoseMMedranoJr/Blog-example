# ATM Challenge Requirements:
# User login with pin
# account selection
# view balance
# deposit
# withdraw
# logout
accounts = [
  {
    "first_name": "Diana",
    "last_name": "Wilson",
    "account_number": "4857291034",
    "pin": "7302",
    "accounts": {
      "checking": 1245.91,
      "savings": 15602.87,
    }
  }
]

class ATM: 

    def __init__(self,  account_number, pin, card_inserted):
        self.account_number = account_number
        self.pin = pin 
        self.card_inserted = card_inserted

    def deposit(self, amount):
        check_bal = accounts["accounts"[0]]
        dep_amount = amount
        balance = dep_amount + check_bal 
        print(check_bal))

  


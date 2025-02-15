# Enhanced Bank Account Management System

# 🏦 Data Structures to Store Information
account_holders = []  # Account names
balances = []         # Account balances
transaction_histories = []  # Account transaction logs
loans = []            # Account loan details
account_index = 0

MAX_LOAN_AMOUNT = 10000
INTEREST_RATE = 0.03

def display_menu():
    """Main menu for banking system."""
    print("\n🌟 Welcome to World Bank System 🌟")
    print("1️⃣ Create Account")
    print("2️⃣ Deposit Money")
    print("3️⃣ Withdraw Money")
    print("4️⃣ Check Balance")
    print("5️⃣ List All Accounts")
    print("6️⃣ Transfer Funds")
    print("7️⃣ View Transaction History")
    print("8️⃣ Apply for Loan")
    print("9️⃣ Repay Loan")
    print("🔟 Identify Credit Card Type")
    print("0️⃣ Exit")

def create_account():
    """Create a new account."""
    user_name = input("Your Name: ")

    for user in account_holders:
        if user.lower() == user_name.lower():
            print("======== This name is already taken! ========"
                  "\n======== Please try again with a different name. ========")
            return

    account_holders.append(user_name)
    balances.append(0)
    loans.append(0)
    print(f"Hello {user_name}, please select the action you want to perform.")
    account_index = account_holders.index(user_name)
    print(account_holders)


def deposit():
    """Deposit money into an account."""
    deposit_money = int(input("Please enter an integer: "))
    balances[account_index] += deposit_money
    print(f'The amount you loaded into your account {deposit_money}\n'
          f'Total amount in your account {balances[account_index] }')


def withdraw():
    """Withdraw money from an account."""
    withdraw_money = int(input("Please enter an integer: "))
    if withdraw_money > balances[account_index]:
        print(f'There is not enough money in your account!!!\n'
              f'Try a new amount.')
        withdraw()
    else:
        balances[account_index]  -= withdraw_money
        print(f"The amount of money you withdraw {withdraw_money}\n"
              f"The amount of money remaining in your account {balances[account_index]}")

def check_balance():
    """Check balance of an account."""
    print(f'======== Your balance: {balances[account_index]} ========')

def list_accounts():
    """List all account holders and details."""
    for index in  range(len(account_holders)):

        print(f'{index + 1}: {account_holders[index]}')

def transfer_funds():
    """Transfer funds between two accounts."""
    pass  # TODO: Add logic

def view_transaction_history():
    """View transactions for an account."""
    pass  # TODO: Add logic

def apply_for_loan():
    """Allow user to apply for a loan."""
    loan = int(input())
    loans[account_index] -= loan
    balances[account_index] += loan

def repay_loan():
    """Allow user to repay a loan."""
    pass  # TODO: Add logic

def identify_card_type():
    """Identify type of credit card."""
    pass  # TODO: Add logic

def main():
    """Run the banking system."""
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        # Map choices to functions
        if choice == 1:
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transaction_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            identify_card_type()
        elif choice == 0:
            print(f"Goodbye! 👋" )
            break
        else:
            print("❌ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
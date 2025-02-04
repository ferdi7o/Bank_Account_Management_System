### **🌟 Bank Account Management System 🌟**

![12291285_Startup-managers-presenting-and-analyzing-sales-growth-chart-1024x683](https://miro.medium.com/v2/resize:fit:1200/1*Rz-2ufGoJ5vZZPjML357eA.jpeg)

#### **🎯 Learning Goals**
1. **Understand Core Programming Concepts**: Functions, loops, conditional statements, and lists.
2. **Work with Python for Real-Life Applications**: Simulate a bank management system with real-world features.
3. **Learn Modular Programming**: Design reusable and well-structured code.
4. **Enhance Debugging Skills**: Test each function using various edge cases.
5. **Version Control and Collaboration**: Use GitHub for submission, version tracking, and feedback.
6. **Critical Thinking**: Implement a credit card type checker and integrate it with other features.

---

### **📁 Project Structure**

```plaintext
EnhancedBankSystem/
├── main.py                # Main program file
├── README.md              # Project documentation
├── test/                  # Folder for testing scripts
│   ├── test_main.py       # Unit tests for all functions
├── submission/            # Folder where students push GitHub URLs
│   ├── student1.txt       # URL of Student 1's GitHub repository
│   ├── student2.txt       # URL of Student 2's GitHub repository
└── .gitignore             # File to exclude unnecessary files from Git tracking
```

---

**1️⃣ Tasks and Features**
1. **Create a Bank Account**
   - Prompt user for account name.
   - Add account with `0` balance and initialize a loan amount to `0`.

2. **Deposit Money**
   - Verify the account exists.
   - Update the balance and log the transaction.

3. **Withdraw Money**
   - Ensure sufficient balance exists for the withdrawal.
   - Update the balance and log the transaction.

4. **Check Balance**
   - Display the account's current balance.

5. **List All Accounts**
   - List account holders with their balance and loan details.

6. **Transfer Funds**
   - Allow money transfers between accounts if sufficient balance exists.

7. **Transaction History**
   - View all past transactions for an account.

8. **Apply for a Loan**
   - Allow loan applications up to `MAX_LOAN_AMOUNT` and calculate interest.

9. **Repay a Loan**
   - Deduct loan amounts from balance upon repayment.

10. **Identify Credit Card Type**
    - Check if the card is Visa, Mastercard, or another type based on number prefixes.

11. **Exit the System**
    - Terminate the program gracefully.

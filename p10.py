import streamlit as st

st.title("ATM Machine")

class Bank:
    def __init__(self):
        self.acc_bal = 10000
        self.withdrawal_count = 0

    def deposit(self, amount):
        if amount < 100:
            st.error("Deposit amount must be at least 100.")
        elif amount > 20000:
            st.error("Deposit amount cannot exceed 20,000.")
        elif amount % 100 != 0:
            st.error("Deposit amount must be a multiple of 100.")
        else:
            self.acc_bal += amount
            st.success(f"Successfully deposited {amount}. New balance: {self.acc_bal}")

    def withdraw(self, amount):
        if self.withdrawal_count >= 3:
            st.error("Withdrawal transaction limit reached. You can only perform 3 withdrawals.")
        elif amount < 100:
            st.error("Withdrawal amount must be at least 100.")
        elif amount > 20000:
            st.error("Withdrawal amount cannot exceed 20,000.")
        elif amount % 100 != 0:
            st.error("Withdrawal amount must be a multiple of 100.")
        elif amount > (self.acc_bal - 500):
            st.error("You must maintain a minimum balance of 500.")
        elif amount <= self.acc_bal:
            self.acc_bal -= amount
            self.withdrawal_count += 1
            st.success(f"Successfully withdrew {amount}. New balance: {self.acc_bal}")
        else:
            st.error("Insufficient balance.")

    def tot_balance(self):
        st.success(f"Your current balance is: {self.acc_bal}")

    def validate_pin(self, pin):
        if pin == 1234:
            return True
        return False

obj = Bank()

if 'pin_attempts' not in st.session_state:
    st.session_state.pin_attempts = 0


if 'bank' not in st.session_state:
    st.session_state.bank = obj


if st.session_state.pin_attempts >= 3:
    st.error("Too many invalid attempts. Your account is locked.")
    st.stop()

pin = st.text_input("Enter your PIN", type="password")
if pin:
    if st.session_state.bank.validate_pin(int(pin)):
        st.success("PIN validated successfully!")
        option = st.selectbox("Choose an option", ("Deposit", "Withdraw", "Balance Enquiry", "Exit"))

        if option == "Deposit":
            deposit_amount = st.number_input("Enter the amount to deposit", min_value=100, max_value=50000, step=100)
            if st.button("Deposit"):
                st.session_state.bank.deposit(deposit_amount)

        elif option == "Withdraw":
            withdraw_amount = st.number_input("Enter amount to withdraw", min_value=100, max_value=20000, step=100)
            if st.button("Withdraw"):
                st.session_state.bank.withdraw(withdraw_amount)

        elif option == "Balance Enquiry":
            st.session_state.bank.tot_balance()

        elif option == "Exit":
            st.info("Thank you for using the ATM. Goodbye!")
            st.session_state.pin_attempts = 0
            st.stop()

    else:
        st.session_state.pin_attempts += 1
        st.error(f"Invalid PIN. Attempts left: {4 - st.session_state.pin_attempts}")

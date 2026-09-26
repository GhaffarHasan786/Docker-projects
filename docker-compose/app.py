
import psycopg2
import time


# =========================
# Database Configuration
# =========================

DB_CONFIG = {
    "host": "db-server",
    "database": "bankdb",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}


# =========================
# Connect to PostgreSQL
# =========================

def connect_to_database():
    max_retries = 5

    for attempt in range(1, max_retries + 1):
        try:
            connection = psycopg2.connect(**DB_CONFIG)
            print("✅ Connected to PostgreSQL database.")
            return connection

        except psycopg2.OperationalError:
            print(
                f"❌ Database connection failed "
                f"(Attempt {attempt}/{max_retries})"
            )

            if attempt < max_retries:
                print("⏳ Retrying in 3 seconds...")
                time.sleep(3)

    print("❌ Could not connect to database.")
    return None


# =========================
# Create Account Table
# =========================

def create_table(connection):
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            balance NUMERIC(12, 2) DEFAULT 0.00
        )
    """)

    connection.commit()
    cursor.close()


# =========================
# Create Default Account
# =========================

def create_default_account(connection):
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM accounts LIMIT 1")

    account = cursor.fetchone()

    if account is None:
        cursor.execute(
            """
            INSERT INTO accounts (name, balance)
            VALUES (%s, %s)
            """,
            ("Ghaffar", 0.00)
        )

        connection.commit()
        print("👤 Default account 'Ghaffar' created.")

    cursor.close()


# =========================
# Check Balance
# =========================

def check_balance(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name, balance
        FROM accounts
        LIMIT 1
    """)

    account = cursor.fetchone()

    if account:
        name, balance = account

        print("\n------------------------")
        print(f"Account : {name}")
        print(f"Balance : ${balance:.2f}")
        print("------------------------")

    cursor.close()


# =========================
# Deposit Money
# =========================

def deposit(connection):
    try:
        amount = float(input("Enter deposit amount: $"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        cursor = connection.cursor()

        cursor.execute("""
            UPDATE accounts
            SET balance = balance + %s
            WHERE id = (
                SELECT id FROM accounts LIMIT 1
            )
        """, (amount,))

        connection.commit()
        cursor.close()

        print(f"✅ ${amount:.2f} deposited successfully.")

    except ValueError:
        print("❌ Please enter a valid amount.")


# =========================
# Withdraw Money
# =========================

def withdraw(connection):
    try:
        amount = float(input("Enter withdrawal amount: $"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        cursor = connection.cursor()

        cursor.execute("""
            SELECT balance
            FROM accounts
            LIMIT 1
        """)

        balance = cursor.fetchone()[0]

        if amount > float(balance):
            print("❌ Insufficient balance.")
            cursor.close()
            return

        cursor.execute("""
            UPDATE accounts
            SET balance = balance - %s
            WHERE id = (
                SELECT id FROM accounts LIMIT 1
            )
        """, (amount,))

        connection.commit()
        cursor.close()

        print(f"✅ ${amount:.2f} withdrawn successfully.")

    except ValueError:
        print("❌ Please enter a valid amount.")


# =========================
# Main Application
# =========================

def main():

    print("==============================")
    print("     PYTHON BANKING SYSTEM")
    print("==============================")

    connection = connect_to_database()

    if connection is None:
        return

    create_table(connection)
    create_default_account(connection)

    # Interactive Menu
    while True:

        print("\n========== MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(connection)

        elif choice == "2":
            deposit(connection)

        elif choice == "3":
            withdraw(connection)

        elif choice == "4":
            print("👋 Thank you for using the banking system.")
            break

        else:
            print("❌ Invalid choice. Please select 1-4.")

    connection.close()
    print("🔌 Database connection closed.")


# =========================
# Run Application
# =========================

if __name__ == "__main__":
    main()
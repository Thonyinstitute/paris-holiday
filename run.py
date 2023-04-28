# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import pyfiglet
import gspread
from google.oauth2.service_account import Credentials

"""
Google API calling, the url and the attributes
"""
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file", 
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('paris_holiday')

expense = SHEET.worksheet('expense') # expense is declared
data = expense.get_all_values() # call to get data values from expense data
print(data)

"""
Google API Verification and figlet print out
"""
print(pyfiglet.figlet_format('Welcome to Paris'))

def get_expense_data():
    """
    Requesting expense from user
    """
    while True:
        print("Please enter travelling documents.")
        print("Documents must be three type only.")
        print("Documents Type are: Passport, Ticket, Money.")


        data = input("Enter your documents here: ")
        print(f"The documents provided are {data}")

        expense_data = data.split(",")
        if validate_data(expense_data): 
            print("Documents are submitted successfully")
            break 
        return expense_data

def validate_data(values):
    print(values) #  expense data values are printed out
    """
    Raise Value error if data values lenght are more than required
    
    """
    try:
        if len(values) != 3:
            raise ValueError(
                f"Three values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid documents: {e}, please try again")
        return False
    return True

data = get_expense_data() # this is the call for expense data values





# coding: utf-8
import csv
from inspect import currentframe
from pathlib import Path

import csv
from optparse import Values
from pathlib import Path

"""Part 2: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list

# function to figure out how many loans there are
total_number_of_loans = len(loan_costs)
# print the amount of loans
print(f"There are {total_number_of_loans} loan costs.")

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans

# function to figure out the total of all loans added together
total_of_all_loans = sum(loan_costs)
# print the total amount of all the loans added together
print(f"The total cost of all the loans is ${total_of_all_loans}.")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount

# function to figure out the average price of all the loans
average_loan_price = total_of_all_loans / total_number_of_loans
# print the average price of all the loans
print(f"The average loan cost is ${average_loan_price}.")

"""Part 3: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, 
or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and 
**Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan
    (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully
    repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required
return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the
loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that 
    says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says 
    that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does 
    it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and 
# Remaining Months on the loan.
# Print each variable.

# get the cost of the loan from the dictionary
loan_price = loan.get("loan_price")
# print the cost of the loan
print(f"The loan price is ${loan_price}.")

# get the amound of months remaining on the loan from the dictionary
remaining_months = loan.get("remaining_months")
# print the amount of months remaining
print(f"There are {remaining_months} months remaining in the loan term.")

# get the future value of the loan from the dictionary
future_value = loan.get("future_value")
# print the future value of the loan
print(f"The future value is ${future_value}.")

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# add a variable for the discount rate
discount_rate = 0.20
# function to find the present value of the loans
present_value = future_value / (1 + (discount_rate/12)) ** remaining_months

# print the present value of the loan
print(f"The present value of the loan is ${present_value:.2f}.")

# If Present Value represents what the loan is really worth, does it make sense to buy the loan 
# at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value 
# represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message 
# that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that 
# says that the loan is too expensive and not worth the price.

# if the present value is greater than or equal to the loan price, then print a statement that it's worth purchasing the loan
if present_value >= loan_price:
    print("The loan is worth at least the cost to buy it.")
    print("Since the cost of the loan is less than or equal to the current fair value, it makes sense to buy this loan.")
# if not, then print a statement that the loan is not worth purchasing
else:
    print("The loan is too expensive and not worth the price.")
    print("Since the cost of the loan is greater than the current fair value, it does not make sense to buy this loan.")



"""Part 4: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the 
    `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""



# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# define a new function that can be reused to find the present value of a monthly loan
def value(remaining_months, annual_discount_rate, future_value):
    present_value = future_value / (1 + (annual_discount_rate/12)) ** remaining_months
    # return the present value
    return present_value

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the 
# `annual_discount_rate`
#    The function should return the `present_value` for the loan.

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

# use the defined function "value" to find the present value of a given loan
present_value = value(remaining_months = 12, annual_discount_rate = 0.20, future_value = 1000)

# print the present value of a given loan
print(f"The present value of the new loan is ${present_value:.2f}.")


"""Part 5: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the 
inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 
    or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the 
    `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""



loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`

# make a new empty list called "inexpensive loans"
inexpensive_loans = [] 

# @TODO: Loop through all the loans and append any that cost $500 or less to the 
# `inexpensive_loans` list

# if the loans are less than or equal to 500, then add them to the new "inexpensive_loans" list
for item in loans:
    if item['loan_price'] <= 500:
        inexpensive_loans.append(item)

# @TODO: Print the `inexpensive_loans` list

# print the new "inexpensive_loans" list
print(inexpensive_loans)



"""Part 6: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header

# create a header bar for the new csv file 
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path

# set a desired path for the new csv file
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.

# print a sentence showing that the file is in process of being created
print("Writing the data to a CSV file...")

# open a path for the new csv file using the 'with open' function
with open(output_path, 'w', newline='') as csvfile:
    # denote that a new csv file will be written and commas will be used in between list items
    csvwriter = csv.writer(csvfile, delimiter=",")
    # firstly, write the header at the top of the file
    csvwriter.writerow(header)
    # write the values of the list items in "inexpensive_loans"
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values())
        # print the values in this program for verification
        print(loan.values())
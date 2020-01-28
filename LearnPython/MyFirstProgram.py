"""
This program computes the interest accrued over the specified number of
years on the principal amount with one year as a fixed value for the compound
interval.
"""

# Print title of program
print('Interest Calculator:')

# Allow user input for the Amount, ROI, and Year variables
amount = float(input('Principal amount: '))
roi = float(input('Rate of Interest: '))
years = int(input('Duration (no. of years): '))

# Calulate interest based off of total current value
total = (amount * pow(1 + (roi/100), years))
interest = total - amount

# Print the final result
print('\nInterest = %0.2f' %interest)

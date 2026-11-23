# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:05:35 2026

@author: pdhan
"""

import datetime
import calendar

print("=" * 35)
print("       AGE CALCULATOR")
print("=" * 35)

try:
    # Step 1: Get user information
    name = input("Enter your name: ")
    dob_input = input("Enter your DOB (YYYY-MM-DD): ")

    # Step 2: Convert input into date format
    birth_date = datetime.date.fromisoformat(dob_input)

    # Step 3: Get today's date
    today = datetime.date.today()

    # Step 4: Validate date of birth
    if birth_date > today:
        print("Error: Date of birth cannot be in the future.")

    else:
        # Step 5: Calculate age
        years = today.year - birth_date.year
        months = today.month - birth_date.month
        days = today.day - birth_date.day

        # Borrow days from previous month
        if days < 0:
            months -= 1

            previous_month = today.month - 1
            previous_year = today.year

            if previous_month == 0:
                previous_month = 12
                previous_year -= 1

            days_in_month = calendar.monthrange(
                previous_year, previous_month
            )[1]

            days += days_in_month

        # Borrow months from previous year
        if months < 0:
            years -= 1
            months += 12

        # Step 6: Display result
        print("\n" + "=" * 35)
        print("         AGE CALCULATION")
        print("=" * 35)

        print("Name:", name)
        print("Date of Birth:", birth_date)
        print("Your Age:", years, "years,", months,
              "months,", days, "days")

        print("=" * 35)

except ValueError:
    print("Invalid date! Please enter a valid date in YYYY-MM-DD format.")
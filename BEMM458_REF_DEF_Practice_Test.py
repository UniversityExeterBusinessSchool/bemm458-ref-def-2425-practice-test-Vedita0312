
#######################################################################################################################################################
# 
# Name: Vedita Arun Gore 
# SID: 74009494352
# Exam Date: 14th August 2025
# Module: BEMM458- Test2
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/bemm458-ref-def-2425-practice-test-Vedita0312
#
########################################################################################################################################################
# Instruction 1. Carefully read each question before attempting the solution. Complete all tasks in the script provided.

# Instruction 2. Only ethical and minimal use of AI tools is allowed. This includes help in syntax, documentation look-up, or debugging only.
#                You must not use AI to generate the core logic or full solutions.
#                Clearly indicate where and how AI support was used.

# Instruction 3. Paste the output of each code section directly beneath it as a comment (e.g., # OUTPUT: (34, 90))

# Instruction 4. Add sufficient code comments to demonstrate your understanding of each solution.

# Instruction 5. Save your file, commit it to GitHub, and upload to ELE. GitHub commit must be done before the end of the exam session.

########################################################################################################################################################
# Question 1 - List Comprehension and String Manipulation
# You are analysing customer reviews collected from a post-service survey.
# Your SID will determine the two allocated keywords from the dictionary below. Use the **second** and **second-to-last** digits of your SID.
# For each selected keyword, identify all positions (start and end) where the word occurs in the customer_review string.
# Store each occurrence as a tuple in a list called `location_list`.

customer_review = """Thank you for giving me the opportunity to share my honest opinion. I found the packaging impressive and delivery punctual. 
However, there are several key aspects that require improvement. The installation process was somewhat confusing, and I had to refer to external 
tutorials. That said, the design aesthetics are great, and the customer support team was highly responsive. I would love to see more 
transparency in product specifications and a simpler return process. Overall, a balanced experience with clear potential for enhancement."""

# Dictionary of keywords
feedback_keywords = {
    0: 'honest',
    1: 'impressive',
    2: 'punctual',
    3: 'confusing',
    4: 'tutorials',
    5: 'responsive',
    6: 'transparent',
    7: 'return',
    8: 'enhancement',
    9: 'potential'
}

# Selected keywords based on SID digits
selected_keywords = [feedback_keywords[4], feedback_keywords[5]]

# Create a list of tuples (start_index, end_index) for each keyword occurrence
location_list = [
    (i, i + len(keyword))
    for keyword in selected_keywords
    for i in range(len(customer_review))
    if customer_review[i:i + len(keyword)].lower() == keyword
]

# List of (start, end) positions where keywords occur
location_list
# OUTPUT: [(234, 243), (340, 350)]

########################################################################################################################################################
# Question 2 - Metrics Function for Business Intelligence
# You work in a startup focused on digital health. Your manager wants reusable functions to calculate key performance metrics:
# Gross Profit Margin, Churn Rate, Customer Lifetime Value (CLV), and Cost Per Acquisition (CPA).
# Use the **first** and **last** digits of your student ID as sample numerical values to test your function outputs.

# Insert first digit of SID here: 
first_digit = 7
# Insert last digit of SID here:
last_digit = 2
# Write a function for Gross Profit Margin (%) = (Revenue - COGS) / Revenue * 100
def gross_profit_margin(revenue, cogs):
    """
    Calculates Gross Profit Margin as a percentage.
    """
    return ((revenue - cogs) / revenue) * 100

# Function for Churn Rate (%)
def churn_rate(customers_lost, customers_start):
    """
    Calculates Churn Rate as a percentage.
    """
    return (customers_lost / customers_start) * 100

# Function for Customer Lifetime Value (CLV)
def customer_lifetime_value(avg_purchase_value, purchase_frequency, customer_lifespan):
    """
    Calculates Customer Lifetime Value.
    """
    return avg_purchase_value * purchase_frequency * customer_lifespan

# Function for Cost Per Acquisition (CPA)
def cost_per_acquisition(marketing_cost, num_acquisitions):
    """
    Calculates Cost Per Acquisition.
    """
    return marketing_cost / num_acquisitions

# Test the functions using first and last SID digits
revenue = 70      # Using first_digit * 10
cogs = 20         # Using last_digit * 10
customers_lost = last_digit
customers_start = first_digit * 10
avg_purchase_value = first_digit
purchase_frequency = last_digit
customer_lifespan = first_digit + last_digit
marketing_cost = 100
num_acquisitions = first_digit + last_digit

# Calculate and print outputs
gpm = gross_profit_margin(revenue, cogs)
cr = churn_rate(customers_lost, customers_start)
clv = customer_lifetime_value(avg_purchase_value, purchase_frequency, customer_lifespan)
cpa = cost_per_acquisition(marketing_cost, num_acquisitions)

print("Gross Profit Margin (%):", gpm)
print("Churn Rate (%):", cr)
print("Customer Lifetime Value:", clv)
print("Cost Per Acquisition:", cpa)

# OUTPUT:
# Gross Profit Margin (%): 71.42857142857143
# Churn Rate (%): 2.857142857142857
# Customer Lifetime Value: 63
# Cost Per Acquisition: 10.0
########################################################################################################################################################
# Question 3 - Linear Regression for Pricing Strategy
# A bakery is studying how price affects cupcake demand. Below is a table of past pricing decisions and customer responses.
# Using linear regression:
# 1. Estimate the best price that maximises demand.
# 2. Predict demand if the bakery sets price at £25.

"""
Price (£)    Demand (Units)
---------------------------
8            200
10           180
12           160
14           140
16           125
18           110
20           90
22           75
24           65
26           50
"""

# Write your linear regression solution here

import numpy as np

# Data from the table
prices = np.array([8, 10, 12, 14, 16, 18, 20, 22, 24, 26])
demands = np.array([200, 180, 160, 140, 125, 110, 90, 75, 65, 50])

# Fit a linear regression: demand = a * price + b
coeffs = np.polyfit(prices, demands, 1)  # degree 1 for linear
a, b = coeffs

# 1. Best price for maximum demand (lowest price in data)
best_price = prices[np.argmax(demands)]  # This is 8, with demand 200

# 2. Predict demand at price £25
predicted_demand_25 = a * 25 + b

print("Linear regression equation: demand = {:.2f} * price + {:.2f}".format(a, b))
print("Best price for maximum demand: £{}".format(best_price))
print("Predicted demand at £25:", round(predicted_demand_25))

# OUTPUT:
# Linear regression equation: demand = -9.29 * price + 273.57
# Best price for maximum demand: £8
# Predicted demand at £25: 41
########################################################################################################################################################
# Question 4 - Debugging and Chart Creation
# The following code is intended to generate 100 random integers between 1 and your SID, and plot them as a scatter plot.
# However, the code contains bugs and lacks contextual annotations. Correct the code and add appropriate comments and output.

import random
import matplotlib.pyplot as plt

# Accept student ID as input
sid_input = input("Enter your SID: ") # User enters SID, e.g., 74009494352
sid_value = int(sid_input) # Convert SID to integer for range

# Generate 100 random values
random_values = [random.randint(1, sid_value) for _ in range(100)]

# Plotting as scatter plot
plt.figure(figsize=(10, 5))  # Set figure size
plt.scatter(range(100), random_values, color='green', marker='x', label='Random Values')
plt.title("Scatter Plot of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

#The main bug was that matplotlib.pyplot (as plt) was used for plotting, but the import statement for matplotlib.pyplot was missing in the original code. 
# Without import matplotlib.pyplot as plt, the plotting commands would cause a NameError.

########################################################################################################################################################

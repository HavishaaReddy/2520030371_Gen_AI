WEEK 5 - Token Economics, Cost and Rate-Limit Budgeting

This experiment is used to estimate the cost and usage of an LLM-based application before development.

The program takes expected values such as user requests, token usage, and budget limits, then calculates the estimated cost and checks whether the application can handle the expected traffic within the given limits.

Requirements: Python 3.14 and python-dotenv.

Setup:
1. Install Python and the required dependency.
2. Configure the necessary usage and budget values.
3. Verify that all project files are available in the working directory.

Run: python budget.py.

Sample Input:
 Requests per day = 2000
 Input tokens = 1200
 Output tokens = 300
 Peak requests per minute = 30

The output shows the estimated token consumption, expected cost, rate-limit status, and whether the application stays within the specified budget.

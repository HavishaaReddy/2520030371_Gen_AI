WEEK 7 - Autoregression

This experiment is used to demonstrate autoregressive next-token prediction using a language model. A set of input prompts is given to the model and the top predicted next tokens along with their probabilities are generated and stored in a CSV file.

Files:
1. main.py: Main program file.
2. autoregression.py: Contains the logic for generating next-token predictions from the language model.
3. requirements.txt: Contains required Python package information.
4. week7_probability_results.csv: Output file generated after execution.

Setup:
1. Install Python.
2. Install required packages: pip install -r requirements.txt

Run: python main.py

Output: The program processes a set of predefined prompts and generates the top 5 predicted next tokens for each prompt.

The prompts used in this experiment are:
1. The cat is
2. Artificial intelligence is
3. India is a
4. Machine learning helps

For every prompt, the following details are displayed:
1. Rank
2. Candidate Token
3. Token ID
4. Probability

After completion, the results are saved in: week7_probability_results.csv

Result: The experiment demonstrates how a language model performs next-token prediction using an autoregressive approach by assigning probabilities to possible successor tokens and ranking them based on likelihood.

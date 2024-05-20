# Financial Analysis and Vote Counting

This Python script is designed to analyze financial records and vote counting data. It contains two main functionalities:

1. **PyBank**: Analyzing financial records to calculate various financial metrics.
2. **PyPoll**: Modernizing a small town's vote-counting process by analyzing the votes and determining the election winner.

## PyBank

The PyBank script reads a CSV file containing financial data with two columns: "Date" and "Profit/Losses". It performs the following analyses:

- Calculates the total number of months included in the dataset.
- Calculates the net total amount of Profit/Losses over the entire period.
- Calculates the changes in Profit/Losses over the entire period and finds the average of those changes.
- Determines the greatest increase in profits (date and amount) over the entire period.
- Determines the greatest decrease in profits (date and amount) over the entire period.

### Usage

To run the PyBank script, follow these steps:

1. Ensure you have Python installed on your machine.
2. Download the `budget_data.csv` file and place it in the `Resources` directory.
3. Run the `main.py` script.

The script will print the financial analysis results to the terminal and export them to a text file (`financial_analysis.txt`) in the `analysis` directory.

## PyPoll

The PyPoll script reads a CSV file containing poll data with three columns: "Voter ID", "County", and "Candidate". It performs the following analyses:

- Calculates the total number of votes cast.
- Provides a complete list of candidates who received votes.
- Calculates the percentage of votes each candidate won.
- Determines the total number of votes each candidate won.
- Determines the winner of the election based on popular vote.

### Usage

To run the PyPoll script, follow these steps:

1. Ensure you have Python installed on your machine.
2. Download the `election_data.csv` file and place it in the `Resources` directory.
3. Run the `main.py` script.

The script will print the election results to the terminal and export them to a text file (`election_results.txt`) in the `analysis` directory.

## File Structure

- `main.py`: Main Python script containing the PyBank and PyPoll functionalities.
- `Resources`: Directory containing the input CSV files (`budget_data.csv` and `election_data.csv`).
- `analysis`: Directory containing the output text files (`financial_analysis.txt` and `election_results.txt`).



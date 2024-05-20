#Dependencies
import os
import csv

pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

#Specifying the file to read to
csvPath = os.path.join(pwd, "election_data.csv")

#Initializing a dictionary to store the vote counts of the candidates
Candidates = {}

# Initialize variables to store the winner's name and vote count
winner_name = ""
winner_votes = 0

## Open the file using "read" mode. Specify the variable to hold the contents
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') 

# Skip the header row
    next(csvReader)      

# Loop through the rows in the CSV file
    for row in csvReader:
        candidateName = row[2]

        if candidateName in Candidates:
            voteCount = Candidates.get(candidateName)
            Candidates[candidateName] = voteCount + 1

        else:
            Candidates[candidateName]= 1

totalVotes = sum(Candidates.values())


# Prepare election results for printing and writing to file
election_results = (
    "Election Results\n"
    "------------------------------------\n"
    f"Total Votes: {totalVotes}\n"
    "------------------------------------\n"
)

for candidate, votes in Candidates.items():
    votesPercentage = round(votes / totalVotes * 100, 3)
    election_results += f"{candidate}: {votesPercentage}% ({votes})\n"
    # Check if the current candidate has more votes than the current winner
    if votes > winner_votes:
        winner_name = candidate
        winner_votes = votes

election_results += (
    "------------------------------------\n"
    f"Winner: {winner_name}\n"
    "------------------------------------\n"
)

# Print election results in the terminal
print(election_results)

# Export the results to a text file
output_path = os.path.join(pwd, "analysis","election_results.txt")
with open(output_path, 'w') as text_file:
    text_file.write(election_results)
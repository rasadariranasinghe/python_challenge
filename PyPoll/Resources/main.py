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


print("Election Results")
print("------------------------------------")
print("Total Votes:", totalVotes)
print("------------------------------------")
for candidate, votes in Candidates.items():
    votesPercentage = (round(votes/totalVotes*100,3))
    print (f"{candidate} : {votesPercentage}% ({votes})")
     # Check if the current candidate has more votes than the current winner
    if votes > winner_votes:
        winner_name = candidate
        winner_votes = votes
print("------------------------------------")
print (f"Winner: {winner_name}")
print("------------------------------------")
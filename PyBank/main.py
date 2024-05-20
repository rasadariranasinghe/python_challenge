#Dependencies
import os
import csv

pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)

#Specifying the file to read to
csvPath = os.path.join(pwd, "Resources","budget_data.csv")


dateTotal = 0 
profit_losesTotal = 0
PreviousValue = None
changeTotal = 0
Changes = []
Dates = []


# Open the file using "read" mode. Specify the variable to hold the contents
with open(csvPath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') 

# Skip the header row
    next(csvReader)     

# Loop through the rows in the CSV file
    for row in csvReader:

        # Increment the counter for each row (each month)
        dateTotal += 1

        # Add the value in the second column to profit_losesTotal  
        profit_losesTotal += int(row[1])

        # Get the current value in the second column
        currentValue = int (row[1])

        # Store the date corresponding to the current row
        date = row[0]
        Dates.append(date)

       # Calculate the difference from the previous value if it exists
        if PreviousValue is not None:
                
                #Do the calculation
                Change =  currentValue - PreviousValue

                #store the current value as the previous value in the next iteration
                PreviousValue = currentValue

                # Add the current value to the total value
                changeTotal += Change

                Changes.append(Change)
        else:
            PreviousValue = currentValue
       

greatestIncrease =max(Changes) 
greatestDecrease =min(Changes)  

# Find the index of the greatest increase and decrease
index_of_greatest_increase = Changes.index(greatestIncrease)+1
index_of_greatest_decrease = Changes.index(greatestDecrease)+1

# Prepare financial analysis results
financial_analysis = (
    "Financial Analysis\n"
    "---------------------------\n"
    f"Total Months: {dateTotal}\n"
    f"Total: ${profit_losesTotal}\n"
    f"Average Change: ${round(changeTotal/(dateTotal-1), 2)}\n"
    f"Greatest Increase in Profits: {Dates[index_of_greatest_increase]} (${greatestIncrease})\n"
    f"Greatest Decrease in Profits: {Dates[index_of_greatest_decrease]} (${greatestDecrease})\n"
)

# Print financial analysis results in the terminal
print(financial_analysis)

# Export the results to a text file
output_path = os.path.join(pwd, "analysis","financial_analysis.txt")
with open(output_path, 'w') as text_file:
    text_file.write(financial_analysis)
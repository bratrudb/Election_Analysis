# The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Initialize a list for the Candidate names.
candidate_options = []

#Initialize a dictionary for Candidate votes
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to total vote count.
        total_votes += 1
        
        #Print the candidate name from each row
        candidate_name = row[2]

        #If candidate is not included in the candidate_options list
        if candidate_name not in candidate_options:

            #Append the candidate name to the candidate_options list
            candidate_options.append(candidate_name)

            #Create a key for the candidate_votes dictionary
            candidate_votes[candidate_name] = 0

        #Add to each candidate's vote count
        candidate_votes[candidate_name] += 1
    
#Determine the percentage of votes for each candidate
#Iterate through the candidate list
for candidate_name in candidate_votes:
    #Retrieve the vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes.
    vote_percent = float(votes) / float(total_votes) * 100
    #Print the candidate name and percentage of votes.
    print(f'{candidate_name}: received {vote_percent:.1f}% of the vote.')

    #To do: print out each candidate's name, vote count, and percentage of votes to the terminal
    
    #Determine the winning vote count and candidate
    #Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percent > winning_percentage):
        #If true then set winning_count = votes and winning_percent = vote_percent
        winning_count = votes
        winning_percentage = vote_percent
        #Set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

#To do: print out the winning candidate, vote count and percentage to terminal.
winning_candidate_summary = (
    f"--------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------\n"
)
print(winning_candidate_summary)


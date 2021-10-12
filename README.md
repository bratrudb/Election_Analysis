# Election_Analysis
Analysis of the election using Python

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote.

## Resources
  - Data Source: election_results.csv
  - Software: Python 3.6.7, Visual Studio Code

## Election Audit Results
  - How many votes were cast in this congressional election?
      - 369,711 votes
  -  Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
      - County Votes:
          
          Jefferson: 10.5% (38,855)
          
          Denver: 82.8% (306,055)
          
          Arapahoe: 6.7% (24,801)
   - Which county had the largest number of votes?
      - Denver county had that largest number of votes with 306,055 or 82.8% of the total votes.
   - Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
      - Candidate Votes: 
        
        Charles Casper Stockham: 23.0% (85,213)
        
        Diana DeGette: 73.8% (272,892)
        
        Raymon Anthony Doane: 3.1% (11,606)
   
   - Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
       - Diana DeGette won the election with 272,892 or 73.8 percent of the total votes.

## Election-Audit Summary

This script is extremely versatile in it's ability to perform an audit on any election with only slight modifications. If the goal was to review a nationwide presidential election, only slight modifications would be needed to pull the state level that is needed instead of the county level data. If you received a .csv file with an additional column listing state data, all that would be required is to copy the script used to pull the county level data. That includes creating a list to hold each state that voted in the election and creating a dictionary to hold the number of votes from each state. The following code could be used to determine the total number of votes by state:

```python
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # pull each state from the each row.
        state_name = row[X]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

        #Use if statement that pulls each state that does not match a previous state in the state list
        if state_name not in state_options:

            #Add the existing state to the list of states
            state_options.append(state_name)

            # Track the number of votes in each state
            state_options[state_name] = 0

        # Add a vote to that state's vot count.
        state_votes[state_name] += 1
```
You can also modify the code to review election results on a more granular level. Using the same for loop and nested if statements, you can find the number of votes each candidate received in each individual county. In the following example, the code is provided to find each candidate's vote counts in Denver specifically. As with the code used to get the original county and candidate data, you begin by creating a list and dictionary to hold the Denver candidate options and number of votes for each. The following code would then be placed inside of the original for loop.

```python

        # Get candidate and county from each row
        candidate = row[2]
        county_title = row[1]
        
        #If statement looking for Denver in row
        if county_title == "Denver":
            
            #Nested if statement to find if candidate is already in the Denver_options list            
            if candidate not in Denver_options:    
                
                #If not, append candidate
                Denver_options.append(candidate)

                #Track each candidates vote
                Denver_votes[candidate] = 0

            #Add to each candidate's Denver total
            Denver_votes[candidate] += 1
```
You can then print the results of each candidate's vote count in Denver, which returns:

1. Charles Casper Stockham: 57,188

2. Diana DeGette: 239,282

3. Raymon Anthony Doane: 9,585

# Election-Analysis-Challenge
Module 3 Election Analysis Challenge Assignment
## Overview of Election Audit
The purpose of the PyPoll challenge was to use leverage VS Code to analyze a CSV file provided by a Colorado Board of Elections employee requesting an audit of a recent congressional election. 
### Resources:
- Data Source: election_results.csv
- Software: Python, 3.7.6, Microsoft Virtual Studio Code 1.71.1
### Analysis Components:
As part of this audit, the following tasks were required:
  1. Calculate a total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
## Election-Audit Results
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
- How many votes were cast in this congressional election?<br />
  The total number of votes cast in the election was 369,711.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.<br />
  The following excerpt of code was written to conduct this analysis:<br />
 ```
    for candidate_name in candidate_votes:
        # Retrieve vote count and a percentage of votes.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
  ```
   The results were as follows: <br />
   Charles Casper Stockham: 23.0% (85,213)<br />
   Diana DeGette: 73.8% (272,892)<br />
   Raymon Anthony Doane: 3.1% (11,606)<br />
  
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Which county had the largest number of votes?
## Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

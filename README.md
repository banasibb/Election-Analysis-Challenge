# Election-Analysis-Challenge
Module 3 Election Analysis Challenge Assignment
## Overview of Election Audit
The purpose of the PyPoll challenge was to use leverage VS Code to analyze a CSV file provided by a Colorado Board of Elections employee requesting an audit of a recent congressional election. The file provided contained data for approximately 370k votes cast on election day, organized into three columns: Ballot ID, County and Candidate. 
### Resources:
- Data Source: election_results.csv
- Software: Python, 3.7.6, Microsoft Virtual Studio Code 1.71.1
### Analysis Components:
As part of the module coursework (completed prior to the challenge assignment), tasks #1 through #5 below were required. Tasks #6 through #8 were required as part of the PyPoll Challenge :
  1. Calculate a total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calculate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.
  6. Calculate voter turnout for each county.
  7. Calculate the percentage of votes from each county out of the total count.
  8. Determine the county with the highest turnout.
## Election-Audit Results
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
- How many votes were cast in this congressional election?<br />
  The total number of votes cast in the election was 369,711.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.<br />
  Charles Casper Stockham: 23.0% (85,213)<br />
  Diana DeGette: 73.8% (272,892)<br />
  Raymon Anthony Doane: 3.1% (11,606)<br />
  <br />The following excerpt of code was written to conduct this analysis:<br />
 ```
    for candidate_name in candidate_votes:
        # Retrieve vote count and a percentage of votes.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
  ```
  
- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?<br />
    The winner of the election was Diana DeGette, with a total of 272,892 votes or 73.8% of the total votes.<br />
    <br />The following code was required to conduct this analysis and print the results to the terminal: <br />
 ```
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
  ```
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.<br />
    The results for each county are as follows:<br />
     Jefferson: 10.5% (38,855)<br />
     Denver: 82.8% (306,055)<br />
     Arapahoe: 6.7% (24,801)<br />
     <br />The following code was required to conduct this analysis and print the results to the terminal: <br />
 ```
    for county in county_options:
        county_vote = county_votes[county]
        county_vote_percentage = float(county_vote) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n"
            )
        print(county_results, end="")
        txt_file.write(county_results)
  ```
- Which county had the largest number of votes?<br />
    Denver County had the largest voter turnout with 306,055 votes or 82.8% of total votes cast.<br />
     <br />The following code was required to conduct this analysis and print the results to the terminal: <br />
 ```
        if (county_vote > largest_county_turnout_votes) and (
            county_vote_percentage > largest_county_turnout_percentage):
            largest_county_turnout_votes = county_vote
            largest_county_turnout_percentage = county_vote_percentage
            largest_county_turnout = county

    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n"
        )
    print(winning_county_summary)
    txt_file.write(winning_county_summary)
  ```
## Election-Audit Summary
This script could be used to analyze the results of any election, and may be improved upon if it also included an analysis of the total and percentage of total votes by candidate by individual county, which could be used for campaign strategy purposes in future elections. This could help candidates target key geographic areas underserved by their messaging. The analysis may also be improved by the incorporation of the population of each county to identify geographic regions where voter turnout is low. This information could be used to target key areas that may have low percentages of the population that are registered to vote or lack awareness of upcoming elections.


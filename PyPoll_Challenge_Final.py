
# Add Dependencies.
import csv
from distutils import text_file
import os
# Assign a variable for the file to load the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a varible to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Options and declare the empty candidate dictionary.
candidate_options = []
candidate_votes = {}
# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county_turnout = ""
largest_county_turnout_votes = 0
largest_county_turnout_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
    # Get the candidate name from each row.
        candidate_name = row[2]
    # Extract the county name from each row.
        county_name = row[1]

    # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's vote count.
        candidate_votes[candidate_name] += 1
    
    # If the county name does not match any existing county...
        if county_name not in county_options:
            # Add it to the list of counties
            county_options.append(county_name)
            # And begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add a vote to the county's vote count
        county_votes[county_name] += 1
        

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #After opening the file print the final vote count to the terminal
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
# Save the final vote count to the text file.
    txt_file.write(election_results)

    # Creating a header for county results
    candidate_results_header = (
        f"Candidate Results:\n"
    )
    print(candidate_results_header, end="")
    # Save county results header to text file
    txt_file.write(candidate_results_header)

# Save results by candidate to the text file
    for candidate_name in candidate_votes:
        # Retrieve vote count and a percentage of votes.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results, end="")
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
            
    #  Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidates votes to the text file.
    txt_file.write(winning_candidate_summary)

    # Creating a header for county results
    county_results_header = (
        f"County Results:\n"
    )
    print(county_results_header, end="")
    # Save county results header to text file
    txt_file.write(county_results_header)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_options:
    # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]
        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_vote) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({county_vote:,})\n"
            )
        print(county_results, end="")
    # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        



        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote > largest_county_turnout_votes) and (
            county_vote_percentage > largest_county_turnout_percentage):
            largest_county_turnout_votes = county_vote
            largest_county_turnout_percentage = county_vote_percentage
            largest_county_turnout = county

    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"-------------------------\n"
        )
    print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)
# Close the file.
election_data.close()

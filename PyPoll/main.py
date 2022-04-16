import os
import csv

csvpath = os.path.join('C:\\Users\\User\\Desktop\\git-repos\\python-challenge\\PyPoll\\Resources\\election_data.csv')
txtpath = os.path.join('C:\\Users\\User\\Desktop\\git-repos\\python-challenge\\PyPoll\\Analysis\\Analysis.txt')

# Identify variables
total_votes = 0
candidate_list = []
candidate_votes = {}
winner = ""
winning_count = 0


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

with open(csvpath) as csvfile:
   reader = csv.DictReader(csvfile)

   # Loop through data for total votes (overall and by candidate)
   for row in reader:
       total_votes = total_votes + 1
       candidate_nm = row["Candidate"]
       
       if candidate_nm not in candidate_list:
           candidate_list.append(candidate_nm)
           candidate_votes[candidate_nm] = 0
       candidate_votes[candidate_nm] = candidate_votes[candidate_nm] + 1

# Print and write Total Vote results
with open(txtpath, "w") as txt_file:

    vote_results = (
        f"\n\nElection Results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"---------------------------\n"
    )
    print(vote_results)
    txt_file.write(vote_results)

    # Loop through voter data to determine the winner
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(total_votes) * 100

        # Identify winner
        if (votes > winning_count):
            winning_count = votes
            winner = candidate

        # Print and write candidate results
        candidate_results = (f"{candidate}: {vote_percent:.3f}% ({votes})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
    
    # Print  and write winner
    winner_result = (
        f"---------------------------\n"
        f"Total Votes: {winner}\n"
        f"---------------------------\n"    
    )
    print(winner_result)
    txt_file.write(winner_result)         
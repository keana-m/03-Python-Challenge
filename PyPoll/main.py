import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pybank_csv = os.path.join(".", "Resources", "election_data.csv")

voter_id = []
candidates = []
uq_candidate = []
uq_vote_count = []

with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        voter_id.append(row[0])
        candidates.append(row[2])

    total_votes = len(voter_id)
    khan = []
    correy = []
    li = []
    otooley = []

    for candidate in candidates:
        if candidate == "Khan":
            khan.append(candidates)
            khan_votes = len(khan)
            khan_percent = round(khan_votes/total_votes*100,2)
        elif candidate == "Correy":
            correy.append(candidates)
            correy_votes = len(correy)
            correy_percent = round(correy_votes/total_votes*100,2)
        elif candidate == "Li":
            li.append(candidates)
            li_votes = len(li)
            li_percent = round(li_votes/total_votes*100,2)
        else:
            otooley.append(candidates)
            otooley_votes = len(otooley)
            otooley_percent = round(otooley_votes/total_votes*100,2)

    if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
    elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
    elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
    else:
        winner = "O'Tooley"

output_path = os.path.join(".", "Analysis", "election_results.txt")
with open(output_path, 'w') as csvwriter:

    csvwriter.write(f"```text\n")
    csvwriter.write(f"Election Results\n")
    csvwriter.write(f"----------------------------\n")
    csvwriter.write(f"Total Votes: {total_votes}\n")
    csvwriter.write(f"----------------------------\n")
    csvwriter.write(f"Khan: {khan_percent}% ({khan_votes})\n")
    csvwriter.write(f"Correy: {correy_percent}% ({correy_votes})\n")
    csvwriter.write(f"Li: {li_percent}% ({li_votes})\n")
    csvwriter.write(f"O'Tooley: {otooley_percent}% ({otooley_votes})\n")
    csvwriter.write(f"----------------------------\n")
    csvwriter.write(f"Winner: {winner} \n")
    csvwriter.write(f"----------------------------\n")
    csvwriter.write(f"```\n")
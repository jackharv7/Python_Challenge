import os
import csv
#identify variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
o_tooley_votes = 0
khan_percent = 0
correy_percent = 0
li_percent = 0
o_tooley_percent = 0

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Set path for file
csvpath = os.path.join("..", "PyPoll", "election_data.csv")

with open("election_data.csv") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile, None)
    #identify header
    #count each vote for each candidate
    for row in csvreader:
        total_votes += 1
        if row[2] == 'Khan':
            khan_votes += 1
        elif row[2] == 'Correy':
            correy_votes += 1
        elif row[2] == 'Li':
            li_votes += 1
        else:
            o_tooley_votes += 1
#calculate percentages
khan_percent = (khan_votes/total_votes)*100
correy_percent = (correy_votes/total_votes)*100
li_percent = (li_votes/total_votes)*100
o_tooley_percent = (o_tooley_votes/total_votes)*100
#find the winner
if int(khan_votes) > int(correy_votes) and int(khan_votes) > int(li_votes) and int(khan_votes) > int(o_tooley_votes):
    winner = "Khan"
elif int(correy_votes) > int(khan_votes) and int(correy_votes) > int(li_votes) and int(correy_votes) > int(o_tooley_votes):
    winner = "Correy"
elif int(li_votes) > int(correy_votes) and int(li_votes) > int(khan_votes) and int(li_votes) > int(o_tooley_votes):
    winner = "Li"
else:
    winner = "O'Tooley"

text_summary = """
    Election Results
--------------------------
Total Vote: {total_votes}
--------------------------
Khan: {khan_percent:.3f}% ({khan_votes})
Correy: {correy_percent:.3f}% ({correy_votes})
Li: {li_percent:.3f}% ({li_votes})
O'Tooley: {o_tooley_percent:.3f}% ({o_tooley_votes})
--------------------------
    Winner: {winner}
-------------------------- """.format(total_votes=total_votes, khan_percent=khan_percent, khan_votes=khan_votes, correy_percent=correy_percent, correy_votes=correy_votes, li_percent=li_percent, li_votes=li_votes, o_tooley_percent=o_tooley_percent, o_tooley_votes=o_tooley_votes, winner=winner)

print(text_summary)
#write summary to new file
with open('summary.txt', 'w') as outfile:
    outfile.write(text_summary)
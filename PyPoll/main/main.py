import pandas as pd
import os

# Reference to file path
PollFile = os.path.join ("PyPoll","Resources", "election_data.csv")

# read the csv file as a DataFrame
election_data = pd.read_csv(PollFile)

df_ed = pd.DataFrame(election_data)

percent_count = []

# unique candidates
candidates = list(df_ed["Candidate"].unique())

# how many times the candidate appears
counts = list(df_ed["Candidate"].value_counts())

# total vote count
total_votes = sum(counts)

x = 0
# set variable for loop
# for loop to calculate percentages
for candidate in candidates:
    percentage = round(counts[x]/total_votes,3)
    percentage = "{:.3%}".format(percentage)
    percent_count.append(percentage)
    x+=1

# zipp data 
data = list(zip(candidates, percent_count, counts))

# calculate max counts to find winner
max_votes = df_ed["Candidate"].value_counts()

#find max counts
winner_count = max_votes.max()

# put the data into a data frame
df_data = pd.DataFrame(data)

# search for the candidate with the most votes
winner = list(df_data.loc[df_data[2] == winner_count,0])

# rename columns for df_data
sorted_data = df_data.columns = ["Candidate |", "Percent of Votes |", "Vote Count"]

#sort the columns by vote count in descending order
sorted_data = df_data.sort_values("Vote Count", ascending = False)

# print the outputs
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"{sorted_data}")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

# output to a text file
election_winner = open("election_winner.txt","w")
election_winner.write("Election Results/n")
election_winner.write("----------------------/n")
election_winner.write(f"Total Votes: {total_votes}/n")
election_winner.write("----------------------/n")
election_winner.write(f"{sorted_data}/n")
election_winner.write("----------------------/n")
election_winner.write(f"Winner: {winner}/n")
election_winner.write("----------------------/n")

election_winner.close()
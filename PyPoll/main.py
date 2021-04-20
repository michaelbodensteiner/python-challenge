import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

votes = 0          
candidate = []   
khan = int()   
correy = int()   
li = int()  
otooley = int()   

with open(csv_path) as dfile:
    csvreader = csv.reader(dfile, delimiter=',')

    next(csvreader)

    for x in csvreader:
        votes += 1
        candidate.append(x[2])
        if x[2] == "Li":
            li += 1
        if x[2] == "Khan":
            khan += 1
        if x[2] == "Correy":
            correy += 1
        if x[2] == "O'Tooley":
            otooley += 1
   
organize = (set(candidate))
kvotes = float(khan/votes) *100
cvotes = float(correy/votes) *100
lvotes = float(li/votes) *100
ovotes = float(otooley/votes) *100

cand_list = ["Khan", "Correy", "Li", "O'Tooley"]
votes_each = [kvotes, cvotes, lvotes, ovotes]
max_index = votes_each.index(max(votes_each))
winner = cand_list[max_index]

output = ("Election Results\n" 
    "-------------------------\n"
    f"Total Votes: {votes}\n"
    "-------------------------\n"
    f"Khan: {kvotes:.3f}% ({khan})\n"
    f"Correy: {cvotes:.3f}% ({correy})\n"
    f"Li: {lvotes:.3f}% ({li})\n"
    f"O'Tooley: {ovotes:.3f}% ({otooley})\n"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n")

output_path = os.path.join("analysis", "output.txt")

with open(output_path, "w") as txtfile:

    print(output)
    txtfile.write(output)
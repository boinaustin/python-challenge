with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    rows = []
    voter_id = []
    county = []
    candidate = []
    
    
    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            rows.append(row)
            voter_id.append(int(row[0]))
            county.append(str(row[1]))
            candidate.append(str(row[2]))
           
            
df=pd.read_csv(election_data)
pd.DataFrame.groupby
as_index=False
df.groupby(['Candidate']).count()

#votes = ct.Counter()
candidate = candidate[-1]
votes[candidate] += 1 
winner = "Khan"
    
total_number_voter_id = len(rows)
print("Total votes: " + str(total_number_voter_id))
print("--------------------------------------------")
print(df.groupby(['Candidate'],as_index=False).count())
print("--------------------------------------------")
print("Winner: " + str(winner))
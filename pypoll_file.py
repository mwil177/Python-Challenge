import os
import csv

#Path
csvpath = os.path.join('pypoll.csv')

#Open & Read
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    #Read Header 
    csv_header = next(csvreader)
    
    #Establish Variables
    candidates = []
    votes = []
    county = []
    otooley = []
    khan = []
    correy = []
    li = []

    #Read Thru Data Following Header
    for row in csvreader:
       candidates.append(row[2])
       votes.append(int(row[0]))
       county.append(row[2])

    print(f"Election Results") 
    print(f"-------------------------------") 
    print(f"Total Votes")
    vote_total = (len(votes))
    print(vote_total)
    print(f"-------------------------------")
    
   
    #Votes by Candidate
    for candidate in candidates:
        if candidate == "Li":
          li.append(candidates)
          li_votes = len(li)
        elif candidate == "Khan":
          khan.append(candidates)
          khan_votes = len(khan)
        elif candidate == "Correy":
          correy.append(candidates)
          correy_votes = len(correy) 
        else: 
          otooley.append(candidates)
          otooley_votes = len(otooley)
    
    print(li_votes)
    print(khan_votes)
    print(correy_votes)
    print(otooley_votes)
        



    



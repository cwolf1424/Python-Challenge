#modules
import csv

#get file path
data_file_path = "PyPoll/Resources/election_data.csv"

#set variables

total_votes = 0
candidates = []
candidate_votes = []
header = []

#open results
with open (data_file_path) as results:
    #read results
    results_reader=csv.reader(results)
    for vote in results_reader:
        #find header categories
        if (results_reader.line_num ==1):
            header = vote
            print ("Ballot Sections:")
            for section in header:
                print (f'[{header.index(section)}]',section)
            #remove header from vote count
            total_votes -=1
        else:
            #set categores for vote base on header
            ballot_id = vote [0]
            county = vote [1]
            candidate = vote [2]
            #fill candidates list
            if candidate not in candidates:
                candidates.append (candidate)
                candidate_votes.append (1)
            #total votes per candidate
            else:
                current_votes = candidate_votes[candidates.index(candidate)]
                current_votes +=1
                candidate_votes[candidates.index(candidate)] = current_votes  
            total_votes +=1
    print (f'Candidates: {candidates}')
    


#print results
    print ("Election Results")
    print ("-------------------------")
    print (f'Total Votes: {total_votes}')
    print ("-------------------------")
    for candidate in candidates:
        print (f'{candidate}: <cand1_percent>% ({candidate_votes[candidates.index(candidate)]})')
    print ("-------------------------")
    print ("Winner: <winner_name")
    print ("------------------------")

#export results
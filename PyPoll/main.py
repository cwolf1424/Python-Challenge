#modules
import csv

#get file path
data_file_path = "PyPoll/Resources/election_data.csv"

#set variables

total_votes = 0
candidates = []
candidate_votes = []
candidate_percent = []
winner = ""
header = []

#open results
with open (data_file_path) as results:
    #read results
    results_reader=csv.reader(results)
    for vote in results_reader:
        #find header categories
        if (results_reader.line_num ==1):
            header = vote
            ##print ("Ballot Sections:")
            ##for section in header:
            ##    print (f'[{header.index(section)}]',section)
        else:
            #set categores for vote based on header
            ballot_id = vote [0]
            county = vote [1]
            candidate = vote [2]
            #fill candidates list
            if candidate not in candidates:
                candidates.append (candidate)
                candidate_votes.append (1)
            #total votes per candidate
            else:
                candidate_number = candidates.index(candidate)
                current_votes = candidate_votes[candidate_number]
                current_votes +=1
                candidate_votes[candidate_number] = current_votes  
            #add the vote to the votes total
            total_votes +=1
    #figure percents for candidates
    winning_total = 0
    for total in candidate_votes:
        current_percent = ((total/total_votes)*100)
        candidate_percent.append (current_percent)
        if total>winning_total:
            candidate_number = candidate_votes.index(total)
            winning_total = total
            winner = (candidates[candidate_number])            

#print results
    print ("")
    print ("Election Results")
    print ("")
    print ("-------------------------")
    print ("")
    print (f'Total Votes: {total_votes}')
    print ("")
    print ("-------------------------")
    print ("")
    for candidate in candidates:
        candidate_number = candidates.index(candidate)
        print (f'{candidate}: {candidate_percent[candidate_number]}% ({candidate_votes[candidate_number]})')
    print ("")
    print ("-------------------------")
    print ("")
    print (f'Winner: {winner}')
    print ("")
    print ("------------------------")

#export results
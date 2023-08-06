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
        total_votes +=1
    


#print results

##print ("Election Results")
    print ("-------------------------")
    print (f'Total Votes: {total_votes}')
    print ("-------------------------")
##print ("<cand1_name>: <cand1_percent>% (<cand1_vote_count>)")
##print ("-------------------------")
##print ("Winner: <winner_name")
##print ("------------------------")

#export results
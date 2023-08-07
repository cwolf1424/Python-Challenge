# python-challenge
Challenge assignment for Python

#PyBank
--------------------------------------------------


#PyPoll
--------------------------------------------------
Teacher (Benjamen Alford) helped the class with wording of adding candidates.
The following section was from his code:

if (candidate not in candidates):
    candidates.append(candidate)
    candidate_votes.append(1)

I did not re-write it a different way as it didn't really seem like there was a better/different way to do this without re-naming list "candidates" to something that made less sense.

I then used the logic from this help to write my other sections/tracking variables.

--------------------------------------------------
I also used the below section from one of our in-class assignments:

for comic in reader:
    if(reader.line_num ==1):
    header = comic

as the inspiration for the section in my file:

for vote in results_reader:
    #find header_line categories
    if (results_reader.line_num ==1):
        header_line = vote
        ##print ("Ballot Sections:")

--------------------------------------------------
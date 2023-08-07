# python-challenge
Challenge assignment for Python

In both parts of this challenge, I used the formatting form the provided comparison results on the homework instructions for clarity

As it was a similar overall process for both parts of this challenge, I used many of the same notes in both assignments

For simplicity's sake, the sections are layed out in a similar way in both parts of the challenge.


#PyPoll
--------------------------------------------------
Teacher (Benjamen Alford) helped the class with wording of adding candidates.
The following section was from his code:

if (candidate not in candidates):
    candidates.append(candidate)
    candidate_votes.append(1)

I did not re-write it a different way as it didn't really seem like there was a better/different way to do this without re-naming list "candidates" to something that made less sense and it was a relatively small section of code

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

#PyBank
--------------------------------------------------
Used same information as above to write code for header of this section:

for entry in budget_reader:
    if (budget_reader.line_num ==1):
        header_line = entry


#Thank you in advance for any feedback!
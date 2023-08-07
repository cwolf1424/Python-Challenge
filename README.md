# python-challenge
Challenge assignment for Python

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

I also used the following from my Ben:

current_votes =candidate_votes[candidates.index(candidate)]
current_votes = current_votes+1
candidate_votes[candidates.index(candidate)] = current_votes

to inspire my section:

candidate_number = candidates.index(candidate)
current_votes = candidate_votes[candidate_number]
current_votes +=1
candidate_votes[candidate_number] = current_votes  
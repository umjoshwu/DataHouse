# DataHouse
Short coding assignment from DataHouse;
this is the most I could get done in the 2-3 hour time range, including thinking of an idea to score each applicant. 
I considered a variety of ideas, including a weighted scoring system based on the importance of each attribute, but
since the team's duties were not specified, I started to think of more ideas. The weight of each attribute changes with
the team's functions - for example, spice tolerance is much more important in say, a competitive eating team. 

I opted to write a script that finds how different the candidates are to the team members. Basically the script
calculates the maximum difference that a candidate could have between all team members called max_att, and then calculates
how different each candidate is to the team as a whole. How different each candidate is to the team can be very subjective,
and I calculated it by taking the difference in attribute values for all attributes in the applicant and team member.
It uses max_att to normalize the values, and outputs it into a json file. The input is taken in through a file, loaded into
a dictionary data using the json library in python.

Files:
    scorer.py, scores input.json
    input.json, given input
    output.json, output file created by scorer.py
To run:
    python3 scorer.py

My intuition behind this is to create a more well-rounded team, using the ratio of how different each applicant is to 
the team as a whole, only because we do not know the team's duties, and creating a team where everyone has their own strengths
could be very beneficial. However, if we needed a more tight-knit team, we could take smaller ratios as priority.


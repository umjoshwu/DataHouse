import json
from collections import defaultdict

def main():
    # Load data
    with open('input.json', 'r') as f:
        data = json.load(f)

    team = data['team']
    applicants = data['applicants']
    scored_applicants = []

    # Find max difference possible of team
    max_att = 0
    for member in team:
        for attribute, value in member['attributes'].items():
            max_att += max(10 - value, value)

    # Scoring each applicant
    for applicant in applicants:
        name = applicant['name']
        attributes = applicant['attributes']

        # Compare current applicant with each member
        for member in team:
            member_attributes = member['attributes']
            diff = 0

            # Take the difference in each attribute with current member
            for attribute in attributes:
                diff += abs(attributes[attribute] - member_attributes[attribute])

        normal_score = round(diff / max_att, 2)
        scored_applicants.append({
            'name': name,
            'score': normal_score
        })

    # Write scoredApplicants to json
    with open('output.json', 'w') as f:
        json.dump({'scoredApplicants': scored_applicants}, f)

import json

def get_score(applicant, team, max_att):
    attributes = applicant['attributes']
    diff = 0

    # Compare current applicant with each member
    for member in team:
        member_attributes = member['attributes']

        # Take the difference in each attribute with current member
        for attribute in attributes:
            diff += abs(attributes[attribute] - member_attributes[attribute])

    return round(diff / max_att, 2)

def main():
    # Open file & load data
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
        normal_score = get_score(applicant, team, max_att)
        scored_applicants.append({
            'name': name,
            'score': normal_score
        })

    # Write scoredApplicants to json
    with open('output.json', 'w') as f:
        json.dump({'scoredApplicants': scored_applicants}, f)

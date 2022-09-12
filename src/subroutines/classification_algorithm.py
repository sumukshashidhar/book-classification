"""
"""

def evaluate_genre(description, keyword_list):
    point_scores = 0
    total_occurances = 0
    unique_occurances = 0
    for keyword_tuple in keyword_list:
        keyword = keyword_tuple[0]
        points = keyword_tuple[1]
        keyword_occurances = description.count(keyword)
        if keyword_occurances > 0:
            unique_occurances += 1
            point_scores += points
            total_occurances += keyword_occurances
    if unique_occurances == 0:
        return 0
    k = point_scores / unique_occurances
    return total_occurances * k

def score(description, lookup_table):
    # set description to lowercase to avoid issues with matching
    description = description.lower()
    # make a table of scores and genres
    table = {}
    # go through each genre in the lookup table first
    for genre in lookup_table.keys():
        table[genre] = evaluate_genre(description, lookup_table[genre])
    return table

                
                





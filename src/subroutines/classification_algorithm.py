"""
"""
def evaluate_genre(description, keyword_list):
    phrases_seen = set()
    point_scores = 0
    total_occurances = 0
    for keyword_tuple in keyword_list:
        keyword = keyword_tuple[0]
        points = keyword_tuple[1]
        keyword_occurances = description.count(keyword)
        if keyword_occurances > 0:
            # we also need to check if its unique or not, and then add points based on that
            if keyword not in phrases_seen:
                phrases_seen.add(keyword)
                point_scores += points
            total_occurances += keyword_occurances
    # calculate average point score (k) of all occurances
    # look for a short circuit if either point scores or phrases len is 0
    if point_scores == 0 or len(phrases_seen) == 0:
        return 0
    k = point_scores / len(phrases_seen)
    # return the genre score (n * k)
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

                
                





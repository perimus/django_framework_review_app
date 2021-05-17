from typing import List

def calc_average_rating(ratings_list: List[int]) -> int:
    if not ratings_list:
        return 0

    average_rating = round(sum(ratings_list)) / len(ratings_list)
    
    return average_rating

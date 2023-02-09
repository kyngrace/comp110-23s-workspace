"""EX03 - Wordle - Make your best guess!"""
__author__ = "730553137"

being_searched: str = "abc"
being_searched_idx: int = 0

def contains_char(being_searched: str, being_found: str) -> bool:
    """Returns a character that is being searched for"""
    assert len(being_found) == 1
    while being_searched_idx == being_found:
        if being_searched_idx == being_found:
            return True
        else: #being_searched_idx != being_found
            return False       
        
being_searched_idx = being_searched_idx + 1

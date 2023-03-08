"""Practice writing a dict function."""
__author__ = "730553137"

def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Returns a dictionary based on certain inputs."""
    if len(str_list) != len(int_list) or len(str_list) == 0:
        return {}
    else:
        output: str = {}
        for idx in range(len(str_list)):
            output[str_list[idx]] = int_list[idx]
        return output

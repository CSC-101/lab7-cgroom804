# Part 1
from typing import Optional


def str_to_float(string: str) -> Optional[float]:
    try:
        return float(string)
    except:
        return None
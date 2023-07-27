#!/usr/bin/env python3
"""
 function should return a tuple of size two containing
 a start index and an end index corresponding to the 
 range of indexes to return in a list f
 or those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    if page < 1:
        start_in = 0
    else:
        start_in = (page -1) * page_size
        end_in = page * page_size
    return start_in, end_in

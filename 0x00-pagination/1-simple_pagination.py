#!/usr/bin/env python3
"""
 function should return a tuple of size two containing
 a start index and an end index corresponding to the
 range of indexes to return in a list
 for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function should return a tuple of size two
    containing a start index and an end
    index corresponding to the range of indexes to return in
    a list for those particular pagination parameters
    """
    if page < 1:
        start_in = 0
    else:
        start_index = (page - 1) * page_size
        end_index = page * page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        """ Simple pagination mandatory
        Copy index_range from the
        previous task and the following class into your code
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        Server.dataset(self)
        # Or self.dataset()

        if len(self.__dataset) < end_index:
            return []

        return self.__dataset[start_index:end_index]

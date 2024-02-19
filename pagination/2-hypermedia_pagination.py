#!/usr/bin/env python3
"""
    sdadaslkdas;ld sadsahds skljhsjkdhaskjh
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """
        dsdaslkdhjsakldhjsa ksjhsjkhdjs jhjhsd
    """
    start_idx = (page - 1) * page_size
    end_idx = page * page_size
    return (start_idx, end_idx)


class Server:
    """
        skjdnakjsdhsakjhd sadsag gdkjasgd sajdgsa sdsd
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
        """ get page """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        idx_range = index_range(page, page_size)
        dataset_len = len(self.dataset())
        if idx_range[0] >= dataset_len:
            return []
        return self.dataset()[idx_range[0]:idx_range[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ get hyper """

        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = None
        if page + 1 < total_pages:
            next_page = page + 1

        prev_page = None
        if page > 1:
            prev_page = page - 1

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

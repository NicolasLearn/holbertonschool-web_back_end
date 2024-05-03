#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve a hypermedia representation of a dataset
        starting from a specific index.

    Args:
        index (int): The starting index from which to retrieve data.
        page_size (int): The size of each page.

    Returns:
        Dict: Containing hypermedia information and the data starting
        from the specified index.
    """
        assert isinstance(index, int) and isinstance(page_size, int)
        assert 0 <= index < len(self.indexed_dataset())
        assert page_size <= len(self.indexed_dataset())

        data = []
        next_index = index + page_size
        i = index
        while i < next_index:
            if i not in self.indexed_dataset():
                next_index += 1
                i += 1
                continue
            data.append(self.indexed_dataset()[i])
            i += 1

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }

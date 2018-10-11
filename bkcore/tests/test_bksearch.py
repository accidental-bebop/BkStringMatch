"""
Unit tests for 'bktree.BK_Search' and 'bktree.BK_Nearest_Neighbor_Search'
"""
# --- Imports

# BKTree
from bktree import BKTree
from bktree import bk_search
from bktree import bk_nearest_neighbor_search


# --- Test Suites

def test_bk_search():
    """
    Test BK_Search function.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    tree = BKTree(string_list)

    # --- Exercise functionality
    search1 = bk_search('eight', tree, 1)
    search2 = bk_search('eight', tree, 10)
    search3 = bk_search('123456789', tree, 1)
    search4 = bk_search('123456789', tree, 10)
    search5 = bk_search('ffff', tree, 1)
    search6 = bk_search('ffff', tree, 3)

    # --- Check results
    assert len(search1) == 2
    assert search1[0] == 1
    assert search1[1:] == ['eight']
    assert len(search2) == 11
    assert search2[0] == 10
    for value in search2[1:]:
        assert value in string_list
    assert len(search3) == 1
    assert search3[0] == 1
    assert len(search4) == 11
    assert search4[0] == 10
    for value in search4[1:]:
        assert value in string_list
    assert len(search5) == 1
    assert search5[0] == 1
    assert len(search6) == 3
    assert search6[0] == 3
    for value in search6[1:]:
        assert value in ['four', 'five']


def test_bk_nearest_neighbor_search():
    """
    Test BK_Nearest_Neighbor_Search function.
    """
    # --- Preparations

    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    tree = BKTree(string_list)

    # --- Exercise functionality
    search1 = bk_nearest_neighbor_search('eight', tree)
    search2 = bk_nearest_neighbor_search('ter', tree)
    search3 = bk_nearest_neighbor_search('123456789', tree)
    search4 = bk_nearest_neighbor_search('ffff', tree)

    # --- Check results
    assert len(search1) == 2
    assert search1[0] == 0
    assert search1[1:] == ['eight']
    assert len(search2) == 2
    assert search2[0] == 1
    assert search2[1:] == ['ten']
    assert len(search3) == 11
    assert search3[0] == 9
    for value in search3[1:]:
        assert value in string_list
    assert len(search4) == 3
    assert search4[0] == 3
    for value in search4[1:]:
        assert value in ['five', 'four']

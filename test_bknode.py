"""
Unit tests for 'bktree.BKNode'
"""
# --- Imports

# BKTree
from bktree import BKNode

# String distance metrics
from strdistlib import calculate_levenshtein_distance


# --- Test Suites

def test_node_creation():
    """
    Test BKNode init method.
    """
    # --- Preparations
    string = 'test_string'
    string2 = 'test_string2'

    # --- Exercise functionality
    node1 = BKNode(string)
    node2 = BKNode(string2, node1)

    # --- Check results
    assert node1.string == string
    assert node1.children == {}
    assert node1.parent is None

    assert node2.string == string2
    assert node2.children == {}
    assert node2.parent == node1


def test_string(capsys):
    """
    Test BKNode str method.
    """
    # --- Preparations
    string = 'test_string'
    node1 = BKNode(string)

    # --- Exercise functionality
    print(node1)

    # --- Check results
    out = capsys.readouterr()
    assert out[0] == string + '\n'


def test_add_child():
    """
    Test BKNode add_child method.
    """
    # --- Preparations
    string = 'test_string'
    string2 = 'test_string2'
    string3 = 'test_string3'
    string4 = 'test_string_4'
    stringdist1 = str(calculate_levenshtein_distance(string, string2))
    stringdist2 = str(calculate_levenshtein_distance(string2, string3))
    stringdist3 = str(calculate_levenshtein_distance(string, string4))
    node1 = BKNode(string)

    # --- Exercise functionality
    node1.add_child(string2, 'levenshtein')
    node1.add_child(string3, 'levenshtein')
    node1.add_child(string4, 'levenshtein')

    # --- Check results
    assert node1.parent is None
    assert node1.string == string
    assert stringdist1 in node1.children
    assert isinstance(node1.children[stringdist1], BKNode)
    assert node1.children[stringdist1].string == string2
    assert stringdist2 in node1.children[stringdist1].children
    assert isinstance(node1.children[stringdist1].children[stringdist2],
                      BKNode)
    assert node1.children[stringdist1].children[stringdist2].string == string3
    assert stringdist3 in node1.children
    assert isinstance(node1.children[stringdist3], BKNode)
    assert node1.children[stringdist3].string == string4


def test_list_children():
    """
    Test BKNode list_children method.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    root_node = BKNode('start')
    root_node.add_child(string_list)

    # --- Exercise functionality
    root_node.list_children()

    # --- Check results


def test_recursive_search():
    """
    Test BKNode recursive_search method.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    root_node = BKNode('start')
    for string in string_list:
        root_node.add_child(string)
    search_string1 = 'ont'
    search_string2 = 'ten'
    search_string3 = 'nomatchstring'
    search1 = []
    search2 = []
    search3 = []
    search4 = []

    # --- Exercise functionality
    root_node.recursive_search(search_string1, 1, search1, 'levenshtein')
    root_node.recursive_search(search_string2, 1, search2, 'levenshtein')
    root_node.recursive_search(search_string3, 1, search3, 'levenshtein')
    root_node.recursive_search(search_string1, 10, search4, 'levenshtein')

    # --- Check results
    assert len(search1) == 1
    assert search1 == ['one']
    assert len(search2) == 1
    assert search2 == ['ten']
    assert search3 == []
    assert search3 == []
    assert len(search4) == 11
    assert search4[0] == 'start'
    for string in search4[1:]:
        assert string in string_list


def test_recursive_nn_search():
    """
    Test BKNode recursive_nearest_neighbor_search method.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    root_node = BKNode('start')
    for string in string_list:
        root_node.add_child(string)
    search_string1 = 'tenr'
    search_string2 = 'ten'
    search_string3 = '1234567890'
    threshold1 = calculate_levenshtein_distance(search_string1, 'start')
    threshold2 = calculate_levenshtein_distance(search_string2, 'start')
    threshold3 = calculate_levenshtein_distance(search_string3, 'start')
    search1 = {}
    search2 = {}
    search3 = {}

    # --- Exercise functionality
    root_node.recursive_nn_search(search_string1, threshold1,
                                  search1, 'levenshtein')
    root_node.recursive_nn_search(search_string2, threshold2,
                                  search2, 'levenshtein')
    root_node.recursive_nn_search(search_string3, threshold3,
                                  search3, 'levenshtein')

    # --- Check results
    assert len(search1) == 1
    assert search1[1] == ['ten']
    assert len(search2) == 1
    assert search2[0] == ['ten']
    assert len(search3) == 1
    for string in search3[10][1:]:
        assert string in string_list

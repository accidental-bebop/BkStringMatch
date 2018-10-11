"""
Unit tests for 'bktree.BKTree'
"""
# --- Imports

# BKTree
from bktree import BKNode
from bktree import BKTree


# --- Test Suites

def test_tree_creation():
    """
    Test BKTree init method.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    root_string = 'start'
    root_node = BKNode(root_string)

    # --- Exercise functionality
    tree = BKTree(string_list)
    tree_alt = BKTree(string_list, root_node)
    tree_blank = BKTree()

    # --- Check results
    assert tree.root.string == string_list[0]
    assert tree_alt.root.string == root_string
    assert tree_blank.root.string == ''


def test_string(capsys):
    """
    Test BKTree str method.
    """
    # --- Preparations
    string_list = ['one', 'two']
    tree = BKTree(string_list)

    # --- Exercise functionality
    print(tree)

    # --- Check results
    out = capsys.readouterr()
    assert out[0] == string_list[0] + '\n'


def test_list_all(capsys):
    """
    Test BKTree list_all method.
    """
    # --- Preparations

    string_list = ['one', 'two', 'three']
    tree = BKTree(string_list)

    # --- Exercise functionality
    tree.list_all()

    # --- Check results
    out = capsys.readouterr()
    printed_strings = out[0].split('\n')
    for value in string_list:
        assert value in printed_strings


def test_count():
    """
    Test BKTree count method.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    root_string = 'start'
    root_node = BKNode(root_string)
    tree = BKTree(string_list)
    tree_alt = BKTree(string_list, root_node)

    # --- Exercise functionality
    count = tree.count()
    count_alt = tree_alt.count()

    # --- Check results
    assert count == len(string_list)
    assert count_alt == len(string_list) + 1


def test_update():
    """
    Test BKTree update method.
    """
    # --- Preparations
    string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
                   'eight', 'nine', 'ten']
    root_string = 'start'
    update_string_list = ['eleven', 'twelve']
    root_node = BKNode(root_string)
    tree = BKTree(string_list)
    tree_alt = BKTree(string_list, root_node)

    # --- Exercise functionality
    tree.update()
    tree.update(update_string_list)
    tree_alt.update(update_string_list)

    # --- Check results
    assert tree.count() == len(string_list) + len(update_string_list)
    assert tree_alt.count() == \
        len(string_list) + len(update_string_list) + 1

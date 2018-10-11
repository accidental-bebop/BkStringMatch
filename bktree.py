"""
B-K Nearest Neighbor Search Algorithm
"""
# --- Imports

# String distance metrics
from strdistlib import calculate_levenshtein_distance
from strdistlib import calculate_lc_substring_length
from strdistlib import calculate_hamming_distance
from strdistlib import calculate_q_gram_distance
from strdistlib import calculate_jaccard_distance


# --- B-K Tree Classes

class BKNode:
    """
    B-K Tree node class
    """
    distance_metric = {'levenshtein': calculate_levenshtein_distance,
                       'lcs': calculate_lc_substring_length,
                       'hamming': calculate_hamming_distance,
                       'q_gram': calculate_q_gram_distance,
                       'jaccard': calculate_jaccard_distance}

    def __init__(self, string, parent=None):
        self.string = string
        self.parent = parent
        self.children = {}

    def __str__(self):
        return str(self.string)

    def add_child(self, string, metric='levenshtein'):
        """
        Create BKNode from string and add to dictionary of children with key
        equal to string distance from current node.  If value for key exists,
        attempt to add as child of corresponding node.
        """
        edge_weight = BKNode.distance_metric[metric](self.string, string)
        if edge_weight == 0:
            return
        if str(edge_weight) in self.children:
            self.children[str(edge_weight)].add_child(string, metric)
        else:
            self.children[str(edge_weight)] = BKNode(string,
                                                     parent=self)

    def list_children(self):
        """
        Recursively print string values for current node and all child nodes.
        """
        print(self.string)
        for child in self.children:
            self.children[child].list_children()

    def recursive_search(self, search_string, threshold, matches, metric):
        """
        Recursively search nodes for string distances less than or equal to
        threshold value.
        """
        string_distance = BKNode.distance_metric[metric](self.string,
                                                         search_string)
        if string_distance <= threshold:
            matches.append(self.string)
        for child in self.children:
            if int(child) in range(string_distance - threshold,
                                   string_distance + threshold + 1):
                self.children[child].recursive_search(search_string,
                                                      threshold, matches,
                                                      metric)

    def recursive_nn_search(self, search_string, threshold, matches, metric):
        """
        Recursively search nodes for string distances less than or equal to
        lowest observed string distance value.
        """
        string_distance = BKNode.distance_metric[metric](self.string,
                                                         search_string)
        if string_distance == 0:
            matches.clear()
            matches[0] = [self.string]
            return
        if string_distance <= threshold:
            threshold = string_distance
            if string_distance in matches:
                matches[string_distance].append(self.string)
            else:
                matches[string_distance] = [self.string]
            if len(matches) > 1:
                for key in sorted(matches.keys())[1:]:
                    del matches[key]
        for child in self.children:
            if int(child) in range(string_distance - threshold,
                                   string_distance + threshold + 1):
                self.children[child].recursive_nn_search(
                    search_string, threshold, matches, metric)


class BKTree:
    """
    B-K Tree class
    """
    def __init__(self, strings=None, root=None, metric='levenshtein'):
        self.nodes = 0
        self.metric = metric
        if strings is None:
            strings = ['']
        if root is None:
            self.root = BKNode(strings[0])
        else:
            self.root = BKNode(root.string)
            self.nodes += 1
        for string in strings:
            self.root.add_child(string)
            self.nodes += 1

    def __str__(self):
        return str(self.root.string)

    def list_all(self):
        """
        Print all child node strings from tree root node.
        """
        self.root.list_children()

    def count(self):
        """
        Get total number of nodes in tree.
        """
        return self.nodes

    def update(self, strings=None):
        """
        Add nodes to tree with string values from list.
        """
        if strings is None:
            return
        for string in strings:
            self.root.add_child(string, self.metric)
            self.nodes += 1


def bk_search(search_string, tree, threshold=0):
    """
    Search tree for all strings within supplied threshold value from search
    string.

    Parameters
    ----------
    search_string : str
        search string
    tree : BKTree
        tree to search
    threshold : int
        maximum string distance for returned matches

    Return values
    -------------
    matches : list
        list of strings containing matches from tree, where first item is
        threshold value
    """
    matches = [threshold]
    tree.root.recursive_search(search_string, threshold, matches,
                               tree.metric)

    return matches


def bk_nearest_neighbor_search(search_string, tree):
    """
    Search tree for nearest matches to supplied string.

    Parameters
    ----------
    search_string : str
        search string
    tree : BKTree
        tree to search

    Return values
    -------------
    matches : list
        list of strings containing nearest matches from tree, where first item
        is distance from search_string to nearest matches
    """
    threshold = tree.root.distance_metric[tree.metric](search_string,
                                                       tree.root.string)
    matches_dictionary = {}
    matches_dictionary[threshold] = []
    tree.root.recursive_nn_search(search_string, threshold,
                                  matches_dictionary, tree.metric)
    matches = [sorted(matches_dictionary.keys())[0]]
    for value in matches_dictionary[matches[0]]:
        matches.append(value)

    return matches

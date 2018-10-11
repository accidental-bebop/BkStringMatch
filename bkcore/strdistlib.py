"""
String distance algorithm implementations
"""
# --- Imports


# --- String Distance Algorithms

def calculate_levenshtein_distance(string1, string2):
    """
    Compute the minimum number of substitutions, deletions, and additions
    needed to change string1 into string2.

    Parameters
    ----------
    string1 : str
        string to calculate distance from
    string2 : str
        string to calculate distance to

    Return value
    ------------
    prev[-1] : int
        levenshtein distance
    """
    if len(string1) < len(string2):
        return calculate_levenshtein_distance(string2, string1)

    if not string2:
        return len(string1)

    prev = list(range(len(string2) + 1))
    for i, curr1 in enumerate(string1):
        curr = [i + 1]
        for j, curr2 in enumerate(string2):
            insertions = prev[j + 1] + 1
            deletions = curr[j] + 1
            substitutions = prev[j] + (curr1 != curr2)
            curr.append(min(insertions, deletions, substitutions))
        prev = curr

    return prev[-1]


def calculate_lc_substring_length(string1, string2):
    """
    Calculate the number of maximum consecutive symbols shared between two
    input strings.

    Parameters
    ----------
    string1 : str
        string to calculate distance from
    string2 : str
        string to calculate distance to

    Return value
    ------------
    lcsd : int
        longest common substring length
    """
    matrix = [[0] * (1 + len(string2)) for i in range(1 + len(string1))]
    lcsd = 0
    for cursor1 in range(1, 1 + len(string1)):
        for cursor2 in range(1, 1 + len(string2)):
            if string1[cursor1 - 1] == string2[cursor2 - 1]:
                matrix[cursor1][cursor2] = matrix[cursor1 - 1][cursor2 - 1] + 1
                if matrix[cursor1][cursor2] > lcsd:
                    lcsd = matrix[cursor1][cursor2]
            else:
                matrix[cursor1][cursor2] = 0
    return lcsd


def calculate_hamming_distance(string1, string2):
    """
    Calculate the inverse of the minimum number of substitutions required to
    change string1 into string2.

    Parameters
    ----------
    string1 : str
        string to calculate distance from
    string2 : str
        string to calculate distance to

    Return value
    ------------
    hamming : int
        hamming distance

    Exceptions
    ----------
    std::invalid_argument - length of string1 and string2 differ
    """
    hamming = 0
    s1len = len(string1)
    s2len = len(string2)
    if s1len == s2len:
        for i in range(0, s1len):
            if string1[i] == string2[i]:
                hamming = hamming + 1
    else:
        return 'Error: different string lengths'
    return hamming


def generate_q_gram_matrix(string1, string2, q_value):
    """
    Generate a vector of q-gram occurences in two strings given a
    window size of q.

    Parameters
    ----------
    string1 : str
        string to calculate distance from
    string2 : str
        string to calculate distance to
    q_value : int
        size of q-gram window

    Return values
    -------------
    q_gram_matrix1, q_gram_matrix2 : array
        q-gram matrices of respective input strings

    Exceptions
    ----------
    std::invalid_argument - q_value greater than length of string1
    std::invalid_argument - q_value greater than length of string2
    """
    s1len = len(string1)
    s2len = len(string2)
    i = 0
    j = 0
    q_gram_matrix1 = []
    q_gram_matrix2 = []
    if q_value > s1len or q_value > s1len:
        return 'Error: q_value larger than string length'
    for i in range(s1len - q_value + 1):
        q_gram_matrix1.append(string1[i:i + q_value])
    for j in range(s2len - q_value + 1):
        q_gram_matrix2.append(string2[j:j + q_value])

    return q_gram_matrix1, q_gram_matrix2


def calculate_q_gram_distance(string1, string2, q_value):
    """
    Calculate the sum of the absolute differences between two q-gram matricies
    from strings.

    Parameters
    ----------
    string1 : str
        string to calculate distance from
    string2 : str
        string to calculate distance to
    q_value : int
        size of q-gram window

    Return value
    ------------
    q_gram_distance : int
        q-gram distance
    """
    s1len = len(string1)
    s2len = len(string2)
    q_gram_count = 0
    q_gram_matricies = generate_q_gram_matrix(string1, string2, q_value)
    q_gram_matrix1 = q_gram_matricies[0]
    q_gram_matrix2 = q_gram_matricies[1]
    for qgram1, qgram1 in enumerate(q_gram_matrix1):
        for qgram2, qgram2 in enumerate(q_gram_matrix2):
            if qgram1 == qgram2:
                q_gram_count = q_gram_count + 1
    q_gram_distance = ((s1len - q_value + 1) +
                       (s2len - q_value + 1)) - (2 * q_gram_count)
    return q_gram_distance


def calculate_jaccard_distance(string1, string2, q_value):
    """
    Calculate Jaccard distance, where distance is one minues the quotient of
    the number of shared q-grams to the total number of unique q-grams between
    two strings.

    Parameters
    ----------
    string1 : str
        string to calculate distance from
    string2 : str
        string to calculate distance to
    q_value : int
        size of q-gram window

    Return value
    ------------
    jaccard_distace : float
        jaccard distance
    """
    s1len = len(string1)
    s2len = len(string2)
    q_gram_count = 0
    q_gram_matricies = generate_q_gram_matrix(string1, string2, q_value)
    q_gram_matrix1 = q_gram_matricies[0]
    q_gram_matrix2 = q_gram_matricies[1]
    for qgram1, qgram1 in enumerate(q_gram_matrix1):
        for qgram2, qgram2 in enumerate(q_gram_matrix2):
            if qgram1 == qgram2:
                q_gram_count = q_gram_count + 1
    observed_q_gram = ((s1len - q_value + 1) +
                       (s2len - q_value + 1)) - (q_gram_count)
    jaccard_distance = (1 - (float(q_gram_count)) / observed_q_gram)
    return jaccard_distance

"""
Unit tests for string distance algorithms in 'strdistlib'
"""
# --- Imports

# String distance metrics
from strdistlib import calculate_levenshtein_distance
from strdistlib import calculate_lc_substring_length
from strdistlib import calculate_hamming_distance
from strdistlib import generate_q_gram_matrix
from strdistlib import calculate_q_gram_distance
from strdistlib import calculate_jaccard_distance


# --- Test Suites

def test_levenshtein_distance():
    """
    Test calculations for levenshtein distance.
    """
    # --- Preparations
    string_list = ['kitten', 'sitting', 'flaw', 'lawn', 'Saturday', 'Sunday',
                   'GUMBO', 'GAMBOL', 'levensthein', 'meilenstein', '',
                   '123456789', 'abc', 'ABC']

    # --- Exercise functionality
    result1 = calculate_levenshtein_distance(string_list[0], string_list[1])
    result2 = calculate_levenshtein_distance(string_list[2], string_list[3])
    result3 = calculate_levenshtein_distance(string_list[4], string_list[5])
    result4 = calculate_levenshtein_distance(string_list[6], string_list[7])
    result5 = calculate_levenshtein_distance(string_list[8], string_list[9])
    result6 = calculate_levenshtein_distance(string_list[10], string_list[11])
    result7 = calculate_levenshtein_distance(string_list[10], string_list[0])
    result8 = calculate_levenshtein_distance(string_list[11], string_list[0])
    result9 = calculate_levenshtein_distance(string_list[12], string_list[13])

    # --- Check results
    assert result1 == 3
    assert result2 == 2
    assert result3 == 3
    assert result4 == 2
    assert result5 == 4
    assert result6 == 9 == len(string_list[11])
    assert result7 == 6 == len(string_list[0])
    assert result8 == 9
    assert result9 == 3 == len(string_list[12]) == len(string_list[13])


def test_lc_substring_length():
    """
    Test calculations for longest common substring length.
    """
    # --- Preparations
    string_list = ['ABABC', 'BABCA', 'ABCBA', 'abcXYZ', 'XYZabc', '123456',
                   'test', 'TEST', '']

    # --- Exercise functionality
    result1 = calculate_lc_substring_length(string_list[0], string_list[1])
    result2 = calculate_lc_substring_length(string_list[0], string_list[2])
    result3 = calculate_lc_substring_length(string_list[1], string_list[2])
    result4 = calculate_lc_substring_length(string_list[3], string_list[4])
    result5 = calculate_lc_substring_length(string_list[4], string_list[5])
    result6 = calculate_lc_substring_length(string_list[6], string_list[7])
    result7 = calculate_lc_substring_length(string_list[8], string_list[0])
    result8 = calculate_lc_substring_length(string_list[8], string_list[5])
    result9 = calculate_lc_substring_length(string_list[8], string_list[6])

    # --- Check results
    assert result1 == 4
    assert result2 == 3
    assert result3 == 3
    assert result4 == 3
    assert result5 == 0
    assert result6 == 0
    assert result7 == 0
    assert result8 == 0
    assert result9 == 0


def test_hamming_distance():
    """
    Test calculations for hamming distance.
    """
    # --- Preparations
    string1 = 'flaw'
    string2 = 'lawn'
    string3 = 'test'
    string4 = 'TEST'
    string5 = 'tests'
    string6 = 'stest'

    # --- Exercise functionality
    result1 = calculate_hamming_distance(string1, string2)
    result2 = calculate_hamming_distance(string3, string4)
    result3 = calculate_hamming_distance(string3, string3)
    result4 = calculate_hamming_distance(string3, string5)
    result5 = calculate_hamming_distance(string5, string6)

    # --- Check results
    assert result1 == 0
    assert result2 == 0
    assert result3 == 4 == len(string3)
    assert result4 == 'Error: different string lengths'
    assert result5 == 0


def test_generate_q_gram_matrix():
    """
    Test aux functions for q-gram matrix generation.
    """
    # --- Preparations
    string1 = 'abcde'
    string2 = 'abdcde'

    # --- Exercise functionality
    result1 = generate_q_gram_matrix(string1, string2, 2)
    result2 = generate_q_gram_matrix(string1, string2, 3)
    result3 = generate_q_gram_matrix(string1, string2, 99)

    # --- Check results
    assert len(result1) == 2
    assert result1[0] == ['ab', 'bc', 'cd', 'de']
    assert result1[1] == ['ab', 'bd', 'dc', 'cd', 'de']
    assert len(result2) == 2
    assert result2[0] == ['abc', 'bcd', 'cde']
    assert result2[1] == ['abd', 'bdc', 'dcd', 'cde']
    assert result3 == 'Error: q_value larger than string length'


def test_q_gram_distance():
    """
    Test calculations for q-gram distance.
    """
    # --- Preparations
    string1 = 'abcde'
    string2 = 'abdcde'

    # --- Exercise functionality
    result1 = calculate_q_gram_distance(string1, string2, 2)

    # --- Check results
    assert result1 == 3


def test_jaccard_distance():
    """
    Test calculations for jaccard distance.
    """
    # --- Preparations
    string1 = 'abcde'
    string2 = 'abdcde'

    # --- Exercise functionality
    result1 = calculate_jaccard_distance(string1, string2, 2)

    # --- Check results
    assert result1 == 0.5

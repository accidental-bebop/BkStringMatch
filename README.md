# BkStringMatch

BkStringMatch is a pure-python implementation for efficient string matching and nearest-neighbor searches that leverages BK tree structures by utilizing a variety of string distance metrics.

## Features

* Supports the following distance metrics:
    * Levenshtein distance
    * longest common substring length
    * Hamming distance
    * q-gram distance
    * Jaccard distance
* Supports exact matching, fuzzy searches, and nearest-neighbor searches
* Lightweight codebase and simple syntax

## Installation

```
python setup.py install
```

## Usage

Build tree from list of strings:
```
string_list = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
               'eight', 'nine', 'ten']

tree = BKTree(string_list)
```

Search tree for exact matches:
```
exact_match = bk_search('search-string', tree, 1)
```

Search tree for fuzzy matches with maximum distance of 3:
```
fuzzy_search = bk_search('search-string', tree, 3)
```

Search tree for nearest-neighbor:
```
nn_search = bk_search('search-string', tree)
```

## Testing

```
make test
```

"""Tests for occurrences module - search methods"""
import os
from pygbif import occurrences

def test_search():
    "Basic test of occurrences.search"
    res = occurrences.search(taxonKey = 3329049)
    assert 'dict' == res.__class__.__name__
    assert 5 == len(res)
    assert [u'count', u'endOfRecords', u'limit', u'results', u'offset'] == res.keys()

def test_search_():
    "Basic test of occurrences.search"
    res = occurrences.search(taxonKey = 252408386)
    assert 'dict' == res.__class__.__name__
    assert 24 == len(res)
    assert 252408386 == res['key']

def test_search_():
    "Basic test of occurrences.search"
    res = occurrences.search(taxonKey = 1052909293)
    assert 'dict' == res.__class__.__name__
    assert 5 == len(res)
from nose.tools import *
import sys
sys.path.insert(0, '/Users/yay/Desktop/pyFolder/Projects/simplegame/')
from ex48 import parser

def test_sentence():
	word_list = [('noun', 'princess'), ('verb', 'go'), ('direction', 'north')]
	word_list2 = word_list[:]

	parsed = parser.parse_sentence(word_list)
	parsed2 = parser.Sentence(word_list2[0], word_list2[1], word_list2[2])
	assert_equal(parsed.subject, parsed2.subject)
	assert_equal(parsed.verb, parsed2.verb)
	assert_equal(parsed.object, parsed2.object)

def test_wrong_sentence():
	word_list = [('error', 'I'), ('verb', 'am'), ('error', 'AWESOME')]

	assert_raises(parser.ParserError, parser.parse_sentence, word_list)
import book_analysis
import unittest 

class TestBookAnalysis(unittest.TestCase):
    def test_count_frequency_empty_list(self):
        if 'count_frequency' not in dir(book_analysis):
            self.fail("book_analysis.count_frequency not implemented\n")
        else:
            lst = []
            output = {}
            ret = book_analysis.count_frequency(lst)
            self.assertEqual(len(ret), 0)
            self.assertEqual(ret.items(), output.items())

    def test_count_frequency_1(self):
        if 'count_frequency' not in dir(book_analysis):
            self.fail("book_analysis.count_frequency not implemented\n")
        else:
            lst = ["this", "is", "the", "first", "is", "line", "second", "line", "this"]
            output = {
            "this": 2,
            "is": 2,
            "the": 1,
            "first": 1,
            "line": 2,
            "second": 1
            }
            ret = book_analysis.count_frequency(lst)
            self.assertEqual(len(ret), 6)
            self.assertEqual(ret.items(), output.items())

    def test_count_frequency_3(self):
        if 'count_frequency' not in dir(book_analysis):
            self.fail("book_analysis.count_frequency not implemented")
        else:
            lst = ["this", "is", "the", "first", "line", "this", "is", "the", "second", "line", "with", "random", "punctuations", "this", "is", "the", "third", "line", "poorly", "worded"]
            output = {'this': 3, 'is': 3, 'the': 3, 'first': 1, 'line': 3, 'second': 1, 'with': 1, 'random': 1, 'punctuations': 1, 'third': 1, 'poorly': 1, 'worded': 1}
            ret = book_analysis.count_frequency(lst)
            self.assertEqual(len(ret), 12)
            self.assertEqual(ret.items(), output.items())
    
    def test_count_frequency_4(self):
        if 'count_frequency' not in dir(book_analysis):
            self.fail("book_analysis.count_frequency not implemented")
        else:
            lst = ["word"]
            output = {"word": 1}
            ret = book_analysis.count_frequency(lst)
            self.assertEqual(len(ret), 1)
            self.assertEqual(ret.items(), output.items())
    
    def test_find_most_common_word_1(self):
        if 'find_most_common_word' not in dir(book_analysis):
            self.fail("book_analysis.find_most_common_word not implemented")
        else:
            val = {}
            ret = book_analysis.find_most_common_word(val)
            self.assertEqual(ret, "")
    
    def test_find_most_common_word_2(self):
        if 'find_most_common_word' not in dir(book_analysis):
            self.fail("book_analysis.find_most_common_word not implemented")
        else:
            output = {
                        "this": 2,
                        "is": 2,
                        "the": 1,
                        "first": 1,
                        "line": 2,
                        "second": 1
                    }
            ret = book_analysis.find_most_common_word(output)
            self.assertEqual(ret, "this")
    
    def test_find_most_common_word_3(self):
        if 'find_most_common_word' not in dir(book_analysis):
            self.fail("book_analysis.find_most_common_word not implemented")
        else:
            val = {
                        "this": 3,
                        "is": 3,
                        "the": 3,
                        "first": 1,
                        "line": 3,
                        "second": 1,
                        "with": 10,
                        "random": 1,
                        "punctuations": 1,
                        "third": 1,
                        "poorly": 1,
                        "worded": 1,
                        }
            ret = book_analysis.find_most_common_word(val)
            self.assertEqual(ret, "with")

    def test_get_word_from_line_list_1(self):
        if 'get_words_from_line_list' not in dir(book_analysis):
            self.fail("book_analysis.get_words_from_line_list not implemented")
        else:
            lst = ["This the First-Line.", "This is the Second@Line."]
            ret = book_analysis.get_words_from_line_list(lst)
            self.assertEqual(len(ret), 9)
            self.assertEqual(ret, ["this", "the", "first", "line", "this", "is", "the", "second", "line"])

    def test_get_word_from_line_list_2(self):
        if 'get_words_from_line_list' not in dir(book_analysis):
            self.fail("book_analysis.get_words_from_line_list not implemented")
        else:
            lst = ["This is the first line.", "This is, the second line, with random # punctuations.", "THis is the third line, poorly worded."]
            ret = book_analysis.get_words_from_line_list(lst)
            self.assertEqual(len(ret), 20)
            self.assertEqual(ret, ["this", "is", "the", "first", "line", "this", "is", "the", "second", "line", "with", "random", "punctuations", "this", "is", "the", "third", "line", "poorly", "worded"])

    def test_get_word_from_line_list_3(self):
        if 'get_words_from_string' not in dir(book_analysis):
            self.fail("book_analysis.get_words_from_string not implemented")
        else:
            ret = book_analysis.get_words_from_string("test_input_single_line.txt")
            self.assertEqual(len(ret), 5)
            self.assertEqual(ret, ["test", "input", "single", "line", "txt"])

    def test_get_word_from_line_list_4(self):
        if 'get_words_from_string' not in dir(book_analysis):
            self.fail("book_analysis.get_words_from_string not implemented")
        else:
            ret = book_analysis.get_words_from_string(" This @ is a & single line. ")
            self.assertEqual(len(ret), 5)
            self.assertEqual(ret, ["this", "is", "a", "single", "line"])
    
    def test_get_word_from_line_list_5(self):
        if 'get_words_from_string' not in dir(book_analysis):
            self.fail("book_analysis.get_words_from_string not implemented")
        else:
            ret = book_analysis.get_words_from_string("THIS IS A LINE WITH ALL UPPER CASE CHARACTERS.")
            self.assertEqual(len(ret), 9)
            self.assertEqual(ret, ["this", "is", "a", "line", "with", "all", "upper", "case", "characters"])

    def test_read_file_test_1(self):
        if 'read_file' not in dir(book_analysis):
            self.fail("book_analysis.read_file not implemented")
        else:
            ret = book_analysis.read_file("input_test.txt")
            self.assertEqual(len(ret), 3)

    def test_read_file_test_2(self):
        if 'read_file' not in dir(book_analysis):
            self.fail("book_analysis.read_file not implemented")
        else:
            ret = book_analysis.read_file("shakespeare.txt")
            self.assertEqual(len(ret), 124456)
    
    def test_read_file_test_3(self):
        if 'read_file' not in dir(book_analysis):
            self.fail("book_analysis.read_file not implemented")
        else:
            ret = book_analysis.read_file("test_input_single_line.txt")
            self.assertEqual(len(ret), 1)
            self.assertEqual(ret, ["This is the first line."])


if __name__ == '__main__':
    unittest.main()
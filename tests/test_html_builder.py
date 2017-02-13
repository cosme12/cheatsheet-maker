import os
import sys
import unittest

try:
    sys.path.insert(0, os.path.abspath('..')) #Works for local
    from sheetmaker import html_builder
    from data import test_html_constants
except:
    sys.path.insert(0, os.path.abspath('.'))  #Works for Travis CI
    from sheetmaker import html_builder
    from data import test_html_constants


class HtmlBuilderTestCase(unittest.TestCase):
    """Tests for `html_builder.py`."""

    def test_create_empty_sheet(self):
        """Is empty sheet html created succesfully?"""
        self.title = "title"
        empty_sheet = html_builder.HtmlSheet(self.title, None)
        test_html = empty_sheet.create_empty_sheet()
        self.assertEqual(test_html[0], test_html_constants.TEST_EMPTY_SHEET)
        self.assertEqual(test_html[1], None)


    def test_set_style(self):
        """Is color style created succesfully?"""
        self.title = "title"
        empty_sheet = html_builder.HtmlSheet(self.title, None)
        test_html = empty_sheet.set_style(1)
        self.assertEqual(test_html[0], test_html_constants.TEST_COLOR_STYLE)
        self.assertEqual(test_html[1], "<!-- css -->")


    def test_build_columns(self):
        """Are columns created succesfully?"""
        self.title = "title"
        empty_sheet = html_builder.HtmlSheet(self.title, None)
        test_html = empty_sheet.build_columns(3)
        self.assertEqual(test_html[0], test_html_constants.TEST_COLUMNS)
        self.assertEqual(test_html[1], "<!-- columns -->")


    def test_build_header(self):
        """Is header created succesfully?"""
        self.title = "title"
        empty_sheet = html_builder.HtmlSheet(self.title, None)
        test_html = empty_sheet.build_header("author")
        self.assertEqual(test_html[0], test_html_constants.TEST_HEADER)
        self.assertEqual(test_html[1], "<!-- header -->")


    def test_build_footer(self):
        """Is footer created succesfully?"""
        self.title = "test"
        empty_sheet = html_builder.HtmlSheet(self.title, None, "author")
        test_html = empty_sheet.build_footer("author.png", "http://author.com", "sponsor", "http://sponsor.com")
        self.assertEqual(test_html[0], test_html_constants.TEST_FOOTER)
        self.assertEqual(test_html[1], "<!-- footer -->")


    def test_build_rows_block(self):
        """Is rows block created succesfully?"""
        self.title = "test"
        empty_sheet = html_builder.HtmlSheet(self.title, None)
        test_html = empty_sheet.build_rows_block(1, "block title", 2, ["row1", "row2"])
        self.assertEqual(test_html[0], test_html_constants.TEST_ROWS_BLOCK)
        self.assertEqual(test_html[1], "<!-- column1 -->")


    def test_build_text_block(self):
        """Is text block created succesfully?"""
        self.title = "test"
        empty_sheet = html_builder.HtmlSheet(self.title, None)
        test_html = empty_sheet.build_text_block(2, "block title", "text text text")
        self.assertEqual(test_html[0], test_html_constants.TEST_TEXT_BLOCK)
        self.assertEqual(test_html[1], "<!-- column2 -->")



if __name__ == '__main__':
    unittest.main()


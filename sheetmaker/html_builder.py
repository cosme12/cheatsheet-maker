"""Create html by choosing style, color, blocks, etc.

Todo:
    * 
    * 
"""

class HtmlSheet(object):
	"""The html sheet to be created and customized."""


	def __init__(self, title):
		"""Return a new HtmlSheet object.

		Args:
        	title (str): Html title and file name.
        	date (str): Creation date displayed in footer.        	

		"""
		self.title = title
		self.date = ####################### get today date
	

	def create_empty_sheet(self):
		"""Create a basic html file and a files folder that will be used to make the sheet."""
		pass


	def set_style(self, columns_number, color):
		"""Select the color style, the number of rows and adjust css style that will be used for the html.

		Args:
			columns_number (int): Main rows for the html file (1,2 or 3 only allowed).
        	color (int): Color number for the html style (predefined colors).

		"""
		self.columns_number = columns_number
		self.color = color
		pass


	def build_header(self, author_name, text):
		"""Creates html header.

		Args:	
			author_name (str): Name displayed in header and footer.
			text (str): Extra text to be added in the header.

		"""
		self.author_name = author_name
		pass


	def build_footer(self, author_picture, author_web, sponsor_name, sponsor_web):
		"""Creates html footer.

		Args:
			author_picture (str): Url path to picture, displayed in footer.
        	author_web (str): Url displayed in footer.
        	sponsor_name (str): Name displayed in footer.
        	sponsor_web (str): Url displayed in footer.
		"""
		pass


	def build_rows_block(self, title, rows_number, text):
		"""Creates a html rows block.

		Args:
			title (str): Block title.
			rows_number (int): Numbers of rows to create.
			text (list): Text for each row.

		"""
		pass

	def write_to_file(self, html):
		"""Writes html to file

		Args:
			html (str): Text to write in file.

		"""
		pass

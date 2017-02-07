"""Command line interface handler.

Todo:
    * Add color text in command line
    * Add translation to options
"""

from html_builder import HtmlSheet
import language_strings



class SheetWizard(object):
	"""Creation Wizard for sheet maker.

	Each new html block added will need a new Method to handle each of the
	attributes needed to build it in "html_builder"
	
	"""
	

	def __init__(self, version):
		"""Return a SheetWizard object.
		
		Args:
			version (str): Script version.

		Attrib:
			version (str): Script version.
			lang_strings (dict): Contains all message strings.
			self.title (str): Html file name.
			self.columns (int): Number of main columns.
			NewSheet (obj): HtmlSheet object instance.

		"""
		self.version = version


	def input_handler(self, options):
		"""Handle all inputs. Input validation must be done on each method.

		Args:
			options (dict): Text options that can be selected

		
		Returns:
			answer (str): Text typed by the user.
		"""
		input_text = ""
		for key, value in options.items():
			input_text = "{0}{1}. {2}\n".format(input_text, key, value)
		return(input(input_text))


	def menu_language(self):
		"""Displays language selector"""
		print("Choose your language:")
		options = { 1: "English",
				    2: "Español (NOT CODED YET)",
				  }
		answer = self.input_handler(options)
		if answer == "1":
			self.lang_strings = language_strings.english
		elif answer == "2":
			self.lang_strings = language_strings.espanol
		else:
			self.menu_language()


	def intro(self):
		"""Displays text intro to SheetWizard"""
		print("##################################################################")
		print("#                                                                #")
		print("#                                                                #")
		print("#                 {0} {1}                #".format(self.lang_strings["INTRO_MESSAGE"] ,self.version))
		print("#                                                                #")
		print("#                                                                #")
		print("##################################################################")

	def main_menu(self):
		"""Displays and handles all menu options"""
		print(self.lang_strings["MENU_MESSAGE"])
		options = { 1: "Create sheet",
				    2: "Export (NOT CODED YET)",
				    3: "Help (NOT CODED YET)",
				  }
		answer = self.input_handler(options)
		if answer == "1":
			self.config_sheet()
		elif answer == "2":
			self.export() #not coded yet
		else:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.main_menu()


	def config_sheet(self):
		"""Displays basic sheet styler. Creates a HtmlSheet object instance.

		Method will ask for HtmlSheet attributes.
		"""
		print("##################################################################")
		print(self.lang_strings["CONFIG_SHEET_MESSAGE1"])
		options = { 1: "What is your sheet title? ('CheatSheet' is added automatically)"
				  }
		self.title = self.input_handler(options)
		print(self.lang_strings["CONFIG_SHEET_MESSAGE2"])
		options = { 1: "1 main column",
				    2: "2 main columns",
				    3: "3 main columns"
				  }
		columns = self.input_handler(options)
		if (columns == "1") | (columns == "2") | (columns == "3"):
			self.columns = int(columns)
		else:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.config_sheet()
		print(self.lang_strings["CONFIG_SHEET_MESSAGE3"])
		options = { 1: "Orange",
				    2: "Black and white"
				  }
		color = self.input_handler(options)
		if (color == "1") | (color == "2"):
			color = int(color)
		else:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.config_sheet()

		self.NewSheet = HtmlSheet(self.title) #Creates a HtmlSheet object with title attrib
		self.NewSheet.create_empty_sheet()
		self.NewSheet.set_style(color)
		self.NewSheet.build_columns(self.columns)
		self.add_header()


	def add_header(self):
		"""Displays header options selector"""
		print("##################################################################")
		print(self.lang_strings["HEADER_MESSAGE"])
		options = { 1: "What is the author name?"
				  }
		author_name = self.input_handler(options)
		self.NewSheet.build_header(author_name)
		self.add_footer()


	def add_footer(self):
		"""Displays footer options selector"""
		print("##################################################################")
		print(self.lang_strings["FOOTER_MESSAGE"])
		options = { 1: "What is the author picture url?"
				  }
		author_picture = self.input_handler(options)
		options = { 1: "What is the author website url? (use http://)"
				  }
		author_web = self.input_handler(options)
		options = { 1: "What is the sponsor name?"
				  }
		sponsor_name = self.input_handler(options)
		options = { 1: "What is the sponsor webite url? (use http://)"
				  }
		sponsor_web = self.input_handler(options)
		self.NewSheet.build_footer(author_picture, author_web, sponsor_name, sponsor_web)
		self.add_block()
	

	def add_block(self):
		"""Displays block options selector"""
		print("##################################################################")
		print(self.lang_strings["BLOCK_MESSAGE"])
		options = { 1: "Create text block",
					2: "Create block with rows",
				    0: "Done"
				   }
		answer = self.input_handler(options)
		if answer == "1":
			self.block_text()
		elif answer == "2":
			self.block_rows()
		elif answer == "0":
			self.end()
		else:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.add_block()


	def block_rows(self):
		"""Rows block options selector"""
		print("##################################################################")
		print(self.lang_strings["BLOCK_ROWS_MESSAGE1"])
		print(self.lang_strings["BLOCK_ROWS_MESSAGE2"])
		options = {}
		for i in range(self.columns):
			options[i+1] = str(i+1) + " main column"		
		column_selected = self.input_handler(options)
		if (column_selected == "1") | (column_selected == "2") | (column_selected == "3"):
			column_selected = int(column_selected)
		else:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.block_rows()
		options = { 1: "What is the title of the block?"
				  }
		title = self.input_handler(options)
		options = { 1: "How many rows does it have?"
				  }
		try:
			rows_number = int(self.input_handler(options))
		except:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.block_rows()
		options = { 1: "What is the text of each row? (text row1. # text row2. # text row3)"
				  }
		text = self.input_handler(options)
		text = text.split("#")
		self.NewSheet.build_rows_block(column_selected, title, rows_number, text)
		self.add_block()


	def block_text(self):
		"""Text block options selector"""
		print("##################################################################")
		print(self.lang_strings["TEXT_BLOCK_MESSAGE"])
		print(self.lang_strings["BLOCK_ROWS_MESSAGE2"])
		options = {}
		for i in range(self.columns):
			options[i+1] = str(i+1) + " main column"		
		column_selected = self.input_handler(options)
		if (column_selected == "1") | (column_selected == "2") | (column_selected == "3"):
			column_selected = int(column_selected)
		else:
			print(self.lang_strings["INVALID_INPUT_MESSAGE"])
			self.block_text()
		options = { 1: "What is the title of the block?"
				  }
		title = self.input_handler(options)
		options = { 1: "What is the text for the block (use <br> for new line or any html tag for formatting)"
				  }
		text = self.input_handler(options)
		self.NewSheet.build_text_block(column_selected, title, text)
		self.add_block()

	
	def preview():
		"""Displays preview message"""
		pass


	def export(self):
		"""Displays export options selector"""
		pass

	
	def help():
		"""Displays and handle all help features"""
		pass


	def end(self):
		"""Displays end message and close system"""
		print(self.lang_strings["END_MESSAGE"])



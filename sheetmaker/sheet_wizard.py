"""Command line interface handler.

Todo:
    * Add color text in command line
    * 
"""

class SheetWizard(object):
	"""Creation Wizard for sheet maker.

	Each new html block added will need a new Method to handle each of the
	attributes needed to build it in "html_builder"
	
	"""
	

	def __init__(self, version):
		"""Return a SheetWizard object.
		
		Args:
			version (str): Script version.

		"""
		pass


	def input_handler(self, input_text):
		"""Handle all inputs. Input validation must be done on each method.

		Args:
			input_text (str): text used to display before input is asked.

		
		Returns:
			answer (str): text typed by the user.
		"""
		pass


	def language():
		"""Displays language selector"""
		pass


	def intro():
		"""Displays text intro to SheetWizard"""
		pass


	def menu():
		"""Displays and handles all menu options"""
		pass


	def help():
		"""Displays and handle all help features"""
		pass


	def add_block():
		"""Add block handler"""
		pass


	def block_rows():
		"""Rows block handler"""
		pass


	def add_header():
		"""Add header handler"""
		pass


	def add_footer():
		"""Add footer handler"""
		pass


	def export():
		"""Displays export options selector"""
		pass


	def end():
		"""Displays end message and close system"""
		pass
"""CheatSheet Maker.

This script is used to create cheat sheets or quick reference guides in html. Html sheets can then
be converted to a pdf file, png image or edited by hand.

This script uses the default OS console and guides the user through several questions to build
the sheet style. It's main focus is to be fast and easy to edit results.

"""


import sys
import sheet_wizard


VERSION = "1.1.0"

def main():
    """Main entry point for the script."""
    new_wizard = sheet_wizard.SheetWizard(VERSION)
    new_wizard.menu_language()
    new_wizard.intro()
    new_wizard.main_menu()


if __name__ == '__main__':
    sys.exit(main())

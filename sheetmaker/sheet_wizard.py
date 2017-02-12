"""Command line interface handler.

Todo:
    * Add color text in command line
    * Add translation to options
"""

import datetime
import html_builder
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
            return(self.menu_language())


    def intro(self):
        """Displays text intro to SheetWizard"""
        print("##################################################################")
        print("#                                                                #")
        print("#                                                                #")
        print("#                 {0} {1}              #".format(self.lang_strings["INTRO_MESSAGE"] ,self.version))
        print("#                                                                #")
        print("#                                                                #")
        print("##################################################################")

    def main_menu(self):
        """Displays and handles all menu options"""
        print(self.lang_strings["MENU_MESSAGE"])
        options = { 1: self.lang_strings["MAIN_MENU_OPTIONS"][1],
                    2: self.lang_strings["MAIN_MENU_OPTIONS"][2],
                    3: self.lang_strings["MAIN_MENU_OPTIONS"][3],
                    4: self.lang_strings["MAIN_MENU_OPTIONS"][4],
                  }
        answer = self.input_handler(options)
        if answer == "1":
            self.config_sheet()
        elif answer == "2":
            self.export() #not coded yet
        elif answer == "3":
            self.help() #not coded yet
        elif answer == "4":
            self.end()
        else:
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            return(self.main_menu())


    def config_sheet(self):
        """Displays basic sheet styler. Creates a HtmlSheet object instance.

        Method will ask for HtmlSheet attributes.
        """
        print("##################################################################")
        print(self.lang_strings["CONFIG_SHEET_MESSAGE1"])
        options = { 1: self.lang_strings["CONFIG_SHEET_OPTIONS1"][1],
                  }
        self.title = self.input_handler(options)
        print(self.lang_strings["CONFIG_SHEET_MESSAGE2"])
        options = { 1: self.lang_strings["CONFIG_SHEET_OPTIONS2"][1],
                    2: self.lang_strings["CONFIG_SHEET_OPTIONS2"][2],
                    3: self.lang_strings["CONFIG_SHEET_OPTIONS2"][3],
                  }
        columns = self.input_handler(options)
        if columns in ("1","2","3"):
            self.columns = int(columns)
        else:
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            self.config_sheet()
        print(self.lang_strings["CONFIG_SHEET_MESSAGE3"])
        options = { 1: self.lang_strings["CONFIG_SHEET_OPTIONS3"][1],
                    2: self.lang_strings["CONFIG_SHEET_OPTIONS3"][2],
                    3: self.lang_strings["CONFIG_SHEET_OPTIONS3"][3],
                    4: self.lang_strings["CONFIG_SHEET_OPTIONS3"][4],
                    5: self.lang_strings["CONFIG_SHEET_OPTIONS3"][5],
                    6: self.lang_strings["CONFIG_SHEET_OPTIONS3"][6],
                  }
        color = self.input_handler(options)
        if color in ("1", "2", "3", "4", "5", "6"):
            color = int(color)
        else:
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            return(self.config_sheet())

        self.NewSheet = html_builder.HtmlSheet(self.title, datetime.date.today()) #Creates a HtmlSheet object with title attrib
        new_html = self.NewSheet.create_empty_sheet()
        self.NewSheet.update_html_file(new_html)
        new_html = self.NewSheet.set_style(color)
        self.NewSheet.update_html_file(new_html)
        new_html = self.NewSheet.build_columns(self.columns)
        self.NewSheet.update_html_file(new_html)
        self.add_header()


    def add_header(self):
        """Displays header options selector"""
        print("##################################################################")
        print(self.lang_strings["HEADER_MESSAGE"])
        options = { 1: self.lang_strings["HEADER_OPTIONS"][1],
                  }
        author_name = self.input_handler(options)
        new_html = self.NewSheet.build_header(author_name)
        self.NewSheet.update_html_file(new_html)
        self.add_footer()


    def add_footer(self):
        """Displays footer options selector"""
        print("##################################################################")
        print(self.lang_strings["FOOTER_MESSAGE"])
        options = { 1: self.lang_strings["FOOTER_OPTIONS1"][1],
                  }
        author_picture = self.input_handler(options)
        options = { 1: self.lang_strings["FOOTER_OPTIONS2"][1],
                  }
        author_web = self.input_handler(options)
        options = { 1: self.lang_strings["FOOTER_OPTIONS3"][1],
                  }
        sponsor_name = self.input_handler(options)
        options = { 1: self.lang_strings["FOOTER_OPTIONS4"][1],
                  }
        sponsor_web = self.input_handler(options)
        new_html = self.NewSheet.build_footer(author_picture, author_web, sponsor_name, sponsor_web)
        self.NewSheet.update_html_file(new_html)
        self.add_block()
    

    def add_block(self):
        """Displays block options selector"""
        print("##################################################################")
        print(self.lang_strings["BLOCK_MESSAGE"])
        options = { 1: self.lang_strings["BLOCK_OPTIONS"][1],
                    2: self.lang_strings["BLOCK_OPTIONS"][2],
                    0: self.lang_strings["BLOCK_OPTIONS"][0],
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
            return(self.add_block())


    def block_rows(self):
        """Rows block options selector"""
        print("##################################################################")
        print(self.lang_strings["BLOCK_ROWS_MESSAGE1"])
        print(self.lang_strings["BLOCK_ROWS_MESSAGE2"])
        options = {}
        for i in range(self.columns):
            options[i+1] = str(i+1) + " main column"        
        column_selected = self.input_handler(options)
        if column_selected in ("1","2","3"):
            column_selected = int(column_selected)
        else:
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            return(self.block_rows())
        options = { 1: self.lang_strings["BLOCK_ROWS_OPTIONS1"][1],
                  }
        title = self.input_handler(options)
        options = { 1: self.lang_strings["BLOCK_ROWS_OPTIONS2"][1],
                  }
        try:
            rows_number = int(self.input_handler(options))  #Check if input is an int
        except:
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            return(self.block_rows())
        options = { 1: self.lang_strings["BLOCK_ROWS_OPTIONS3"][1],
                  }
        text = self.input_handler(options)
        if text.count("#") < rows_number - 1: #Deny lower rows text divisor
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            return(self.block_rows())
        text = text.split("#")
        new_html = self.NewSheet.build_rows_block(column_selected, title, rows_number, text)
        self.NewSheet.update_html_file(new_html)
        self.add_block()


    def block_text(self):
        """Text block options selector"""
        print("##################################################################")
        print(self.lang_strings["TEXT_BLOCK_MESSAGE"])
        print(self.lang_strings["BLOCK_ROWS_MESSAGE2"])
        options = {}
        for i in range(self.columns):
            options[i+1] = "{0} {1}".format(str(i+1), self.lang_strings["TEXT_BLOCK_EXTRA"])
        column_selected = self.input_handler(options)
        if column_selected in ("1", "2", "3"):
            column_selected = int(column_selected)
        else:
            print(self.lang_strings["INVALID_INPUT_MESSAGE"])
            self.block_text()
        options = { 1: self.lang_strings["TEXT_BLOCK_OPTIONS1"][1],
                  }
        title = self.input_handler(options)
        options = { 1: self.lang_strings["TEXT_BLOCK_OPTIONS2"][1],
                  }
        text = self.input_handler(options)
        new_html = self.NewSheet.build_text_block(column_selected, title, text)
        self.NewSheet.update_html_file(new_html)
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
        print("##################################################################")
        print(self.lang_strings["END_MESSAGE"])
        input(self.lang_strings["EXIT_MESSAGE"])



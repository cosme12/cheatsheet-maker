"""Create html by choosing style, color, blocks, etc.
Uses html comments <!-- example --> to find the places where to append new html

Todo:
    * 
    * 
"""

class HtmlSheet(object):
    """The html sheet to be created and customized."""


    def __init__(self, title, date):
        """Return a new HtmlSheet object.

        Args:
            title (str): Html title and file name.
            date (str): Today's date.
            

        Attrib:
            title (str): Html title and file name.
            date (str): Creation date displayed in footer.
            color (int): Color code style.
            main_columns (int): Number of columns for sheet structure.
            author_picture (str): Url path to picture, displayed in footer.
            author_web (str): Url displayed in footer.
            sponsor_name (str): Name displayed in footer.
            sponsor_web (str): Url displayed in footer.

        """
        self.title = title
        self.date = date
    

    def create_empty_sheet(self):
        """Create a basic html file and a files folder that will be used to make the sheet."""

        html = """<!DOCTYPE html>
<html class="" lang="en">
    <head>
        <title>{0}</title>
        <style>
            <!-- css -->
        </style>
    </head>
    <body>
        <div id="content">
            <div id="body_inner">
                <div class="main_title_block">
                    <!-- header -->
                </div>
                <table cellspacing="0" cellpadding="0" width="100%">
                    <tbody><tr>
                        <!-- columns -->
                    </tr></tbody>
                </table>
                <div class="block_footer">
                    <!-- footer -->
                </div>
            </div>
        </div>
    </body>
</html>""".format(self.title)
        self.update_html_file(html)


    def set_style(self, color_number):
        """Select the color style, the number of rows and adjust css style that will be used for the html.

        Args:
            color_number (int): Color number for the html style (predefined colors).

        """
        self.color = color_number
        color_main = {1: "#fa6900", #main color
                      2: "#000000",
                     }
        color_secundary = {1: "#fee5d3", #secundary color, lighter than main color
                           2: "#cccccc",
                          }
        html = """
    body {{
        background: #dddfdd none repeat scroll 0 0;
        color: #46473b;
        font-family: "Lucida Grande","Lucida Sans Unicode",Arial,Helvetica,sans-serif;
        font-size: 80%;
        line-height: 1.7;
        margin: 0;
        padding: 0;
        text-align: center;
    }}   
    #content {{
        background: white none repeat scroll 0 0;
        margin: 0 auto;
        padding: 0;
        position: relative;
        text-align: left;
        width: 980px;
    }}   
    #body_inner {{
        padding: 20px;
    }}
    .main_title_block {{
        display: inline-flex;
        margin-bottom: 4%;
    }}
    .main_logo{{
        background-color: #000000;
        border-top: 10px solid {1};
        padding: 10px 20px;
        //width: 50%;
    }}
    .main_title {{
        padding-left: 4%;
        width: 100%;
    }}
    .block {{
        background: {0} none repeat scroll 0 0;
        border-bottom: 3px solid {0};
        border-radius: 3px;
        margin-bottom: 12px;
        padding-bottom: 0;
    }}
    .block_title {{
        //color: #fee5d3;
        color: #ffffff;
        margin: 0;
        padding: 6px 8px;
        text-align: left;
    }}
    i {{
        vertical-align: sub
    }}
    .block_text{{
        padding: 5px 10px;
        background: {1} none repeat scroll 0 0;
    }}
    .rows_table {{
        background: white none repeat scroll 0 0;
        border-collapse: collapse;
        margin: 0;
        padding: 0;
        page-break-inside: avoid;
        width: 100%;
    }}
    .row_even td{{
        background: {1} none repeat scroll 0 0;
        padding: 5px 10px;
    }}
    .row_odd td {{
        padding: 5px 10px;
    }}
    .block_footer {{
        margin-top: 10%;
        border-top: solid 3px #ccc;
        display: inline-flex;
        width: 100%
    }}
    .block_footer_inner {{
        display: inline-flex;
        margin-bottom: 4%;
        margin-left: 4%;
    }}
    .image_footer {{
        width: 64px;
        height: 64px;
        margin-top: 10px;
    }}
    .text_footer{{
        margin-top: 16px;
        margin-left: 10px;
    }}""".format(color_main[self.color], color_secundary[self.color])        
        self.update_html_file(html, "<!-- css -->")

    
    def build_header(self, author_name):
        """Creates html header.

        Args:   
            author_name (str): Name displayed in header and footer.

        """
        self.author_name = author_name
        html = """<a href="http://github.com/cosme12/cheatsheet-maker"><img class="main_logo" src="logo.png"></a>
                <table class="main_title"><tbody><tr><td><h1 style="margin: 0px;">{0} CheatSheet</h1></td></tr>
                    <tr><td>by {1} via CheatSheet Maker</td></tr>
                </tbody></table>""".format(self.title, self.author_name)
        self.update_html_file(html, "<!-- header -->")


    def build_footer(self, author_picture, author_web, sponsor_name, sponsor_web):
        """Creates html footer.

        Args:
            author_picture (str): Url path to picture, displayed in footer.
            author_web (str): Url displayed in footer.
            sponsor_name (str): Name displayed in footer.
            sponsor_web (str): Url displayed in footer.
        """
        self.author_picture = author_picture
        self.author_web = author_web
        self.sponsor_name = sponsor_name
        self.sponsor_web = sponsor_web
        html = """<div class="block_footer_inner">
                    <img class="image_footer" src="{0}">
                    <table class="text_footer"><tbody>
                        <tr><td>By {1}</td></tr>
                        <tr><td><a href="{2}">{2}</a></td></tr>
                    </tbody></table>
                </div>

                <div class="block_footer_inner">
                    <table class="text_footer"><tbody>
                        <tr><td>Created {3}</td></tr>
                        <tr><td><a href="http://github.com/cosme12/cheatsheet-maker">http://github.com/cosme12/cheatsheet-maker</a></td></tr>
                    </tbody></table>
                </div>

                <div class="block_footer_inner">
                    <table class="text_footer"><tbody>
                        <tr><td>Sponsored by {4}</td></tr>
                        <tr><td><a href="{5}">{5}</a></td></tr>
                    </tbody></table>
                </div>""".format(self.author_picture, self.author_name, self.author_web, self.date, self.sponsor_name, self.sponsor_web)
        self.update_html_file(html, "<!-- footer -->")  


    def build_columns(self, columns_number):
        """Creates main_columns html

        Args:
            columns_number (int): Main columns for the html file (1,2 or 3 only allowed).

        """
        self.columns_number = columns_number
        if self.columns_number == 1:
            html = """<td class="column_1" width="100%" valign="top"> <!-- column1 --> </td>"""
        elif self.columns_number == 2:
            html = """<td class="column_1" width="50%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="50%" valign="top"> <!-- column2 --> </td>"""
        elif self.columns_number == 3:
            html = """<td class="column_1" width="32%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column2 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column3 --> </td><td class="column_space" width="2%"></td>"""
        else:
            #error
            pass                        
        self.update_html_file(html, "<!-- columns -->")

    
    def build_rows_block(self, selected_column, title, rows_number, text):
        """Creates a html rows block.

        Args:
            selected_column (int): Column in which block will be created.
            title (str): Block title.
            rows_number (int): Numbers of rows to create.
            text (list): Text for each row.

        """
        rows = ""
        for i in range(rows_number):
            if i % 2 == 0:
                rows += """<tr class="row_even">
                                <td colspan="1" valign="top">
                                    <div>{0}</div>
                                </td>
                            </tr>""".format(text[i])
            else:
                rows += """<tr class="row_odd">
                                <td colspan="1" valign="top">
                                    <div>{0}</div>
                                </td>
                            </tr>""".format(text[i])
        html = """<div class="block">
                    <h3 class="block_title">{0}</h3>
                    <table class="rows_table">
                        <tbody>
                            {1}
                        </tbody>
                    </table>
                </div>""".format(title, rows)
        self.update_html_file(html, "<!-- column" + str(selected_column) + " -->")


    def build_text_block(self, selected_column, title, text):
        """Creates a html text block.

        Args:
            selected_column (int): Column in which block will be created.
            title (str): Block title.
            text (str): Text for block.

        """
        html = """<div class="block">
                    <h3 class="block_title">{0}</h3>
                    <div class="block_text">{1}</div>
                </div>""".format(title, text)
        self.update_html_file(html, "<!-- column" + str(selected_column) + " -->")


    def update_html_file(self, new_html, from_here=None):
        """Reads html file, appends new html and writes it to file

        Args:
            html (str): Text to write in file.
            from_here (str): Text string to continue writting from there.

        """
        #Only reads file if it exists.
        if from_here:
            with open(self.title + ".html", 'r') as sheet:
                html = (sheet.read())
                html = html.replace(from_here, new_html + " " + from_here)
        else:
            html = new_html
        with open(self.title + ".html", 'w') as sheet:
            sheet.write(html)


"""TEST CODE
new = HtmlSheet("prueba")
new.create_empty_sheet()
new.set_style(1)
new.build_header("Cosme12")
new.build_footer("images/dave.jpg", "www.mywebsite.com", "Sponsor Name", "www.sponsor.com")
new.build_columns(3)
text = ["Blocks are organised into columns by you.",
        "PDFs organise blocks into columns automatically.",
        "Try to keep the columns roughly even in length - it makes the cheat sheets easier to use online."]
new.build_rows_block("Block title", 1, 3, text)
"""
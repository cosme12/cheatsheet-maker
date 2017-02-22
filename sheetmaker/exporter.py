"""Export the html sheet to pdf, png or jpeg.

Todo:
    * Add png export
    * Add jpeg export
"""
import pdfkit


class Export(object):
    """docstring for Export"""
    def __init__(self):
        """docstring"""
        path = self.config_read()
        self.path_wkhtmltopdf = r"{0}bin\wkhtmltopdf.exe".format(path)
        self.path_wkhtmltoimage = r"{0}bin\wkhtmltoimage.exe".format(path)


    def to_pdf(self, file_name):
        """Exports html sheet to pdf"""
        config = pdfkit.configuration(wkhtmltopdf=self.path_wkhtmltopdf)
        pdfkit.from_file("{0}.html".format(file_name), "{0}.pdf".format(file_name), configuration=config)


    def to_png(self, file_name):
        """Exports html sheet to png"""
        config = pdfkit.configuration(wkhtmltopdf=self.path_wkhtmltoimage)
        pdfkit.from_file("{0}.html".format(file_name), "{0}.png".format(file_name), configuration=config)

    def config_save(self, path):
        """Saves path to wkhtmltopdf into a file"""
        with open("config.txt", 'w') as config:
            config.write(path)

    def config_read(self):
        """Read path to wkhtmltopdf from file"""
        with open("config.txt", 'r') as config:
            path = (config.read())
            return(path)
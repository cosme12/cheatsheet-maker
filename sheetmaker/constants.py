"""Html Constant file."""

EMPTY_SHEET = """<!DOCTYPE html>
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
</html>"""


COLOR_STYLE = """
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
    }}"""


COLUMNS1 = """<td class="column_1" width="100%" valign="top"> <!-- column1 --> </td>"""
COLUMNS2 = """<td class="column_1" width="50%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="50%" valign="top"> <!-- column2 --> </td>"""
COLUMNS3 = """<td class="column_1" width="32%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column2 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column3 --> </td><td class="column_space" width="2%"></td>"""


HEADER = """<a href="http://github.com/cosme12/cheatsheet-maker"><img class="main_logo" src="example/logo.png"></a>
                <table class="main_title"><tbody><tr><td><h1 style="margin: 0px;">{0} CheatSheet</h1></td></tr>
                    <tr><td>by {1} via CheatSheet Maker</td></tr>
                </tbody></table>"""


FOOTER = """<div class="block_footer_inner">
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
                </div>"""


ROWS_BLOCK_EVEN = """<tr class="row_even">
                                <td colspan="1" valign="top">
                                    <div>{0}</div>
                                </td>
                            </tr>"""
ROWS_BLOCK_ODD = """<tr class="row_odd">
                                <td colspan="1" valign="top">
                                    <div>{0}</div>
                                </td>
                            </tr>"""
ROWS_BLOCK = """<div class="block">
                    <h3 class="block_title">{0}</h3>
                    <table class="rows_table">
                        <tbody>
                            {1}
                        </tbody>
                    </table>
                </div>"""


TEXT_BLOCK = """<div class="block">
                    <h3 class="block_title">{0}</h3>
                    <div class="block_text">{1}</div>
                </div>"""



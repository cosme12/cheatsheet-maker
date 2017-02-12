"""Test html constants"""

TEST_EMPTY_SHEET = """<!DOCTYPE html>
<html class="" lang="en">
    <head>
        <title>title</title>
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

TEST_COLOR_STYLE = """
    body {
        background: #dddfdd none repeat scroll 0 0;
        color: #46473b;
        font-family: "Lucida Grande","Lucida Sans Unicode",Arial,Helvetica,sans-serif;
        font-size: 80%;
        line-height: 1.7;
        margin: 0;
        padding: 0;
        text-align: center;
    }   
    #content {
        background: white none repeat scroll 0 0;
        margin: 0 auto;
        padding: 0;
        position: relative;
        text-align: left;
        width: 980px;
    }   
    #body_inner {
        padding: 20px;
    }
    .main_title_block {
        display: inline-flex;
        margin-bottom: 4%;
    }
    .main_logo{
        background-color: #000000;
        border-top: 10px solid #fee5d3;
        padding: 10px 20px;
        //width: 50%;
    }
    .main_title {
        padding-left: 4%;
        width: 100%;
    }
    .block {
        background: #fa6900 none repeat scroll 0 0;
        border-bottom: 3px solid #fa6900;
        border-radius: 3px;
        margin-bottom: 12px;
        padding-bottom: 0;
    }
    .block_title {
        //color: #fee5d3;
        color: #ffffff;
        margin: 0;
        padding: 6px 8px;
        text-align: left;
    }
    i {
        vertical-align: sub
    }
    .block_text{
        padding: 5px 10px;
        background: #fee5d3 none repeat scroll 0 0;
    }
    .rows_table {
        background: white none repeat scroll 0 0;
        border-collapse: collapse;
        margin: 0;
        padding: 0;
        page-break-inside: avoid;
        width: 100%;
    }
    .row_even td{
        background: #fee5d3 none repeat scroll 0 0;
        padding: 5px 10px;
    }
    .row_odd td {
        padding: 5px 10px;
    }
    .block_footer {
        margin-top: 10%;
        border-top: solid 3px #ccc;
        display: inline-flex;
        width: 100%
    }
    .block_footer_inner {
        display: inline-flex;
        margin-bottom: 4%;
        margin-left: 4%;
    }
    .image_footer {
        width: 64px;
        height: 64px;
        margin-top: 10px;
    }
    .text_footer{
        margin-top: 16px;
        margin-left: 10px;
    }"""

TEST_COLUMNS = """<td class="column_1" width="32%" valign="top"> <!-- column1 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column2 --> </td><td class="column_space" width="2%"></td>
            <td class="column_2" width="32%" valign="top"> <!-- column3 --> </td><td class="column_space" width="2%"></td>"""

TEST_HEADER = """<a href="http://github.com/cosme12/cheatsheet-maker"><img class="main_logo" src="example/logo.png"></a>
                <table class="main_title"><tbody><tr><td><h1 style="margin: 0px;">title CheatSheet</h1></td></tr>
                    <tr><td>by author via CheatSheet Maker</td></tr>
                </tbody></table>"""

TEST_FOOTER = """<div class="block_footer_inner">
                    <img class="image_footer" src="author.png">
                    <table class="text_footer"><tbody>
                        <tr><td>By author</td></tr>
                        <tr><td><a href="http://author.com">http://author.com</a></td></tr>
                    </tbody></table>
                </div>

                <div class="block_footer_inner">
                    <table class="text_footer"><tbody>
                        <tr><td>Created None</td></tr>
                        <tr><td><a href="http://github.com/cosme12/cheatsheet-maker">http://github.com/cosme12/cheatsheet-maker</a></td></tr>
                    </tbody></table>
                </div>

                <div class="block_footer_inner">
                    <table class="text_footer"><tbody>
                        <tr><td>Sponsored by sponsor</td></tr>
                        <tr><td><a href="http://sponsor.com">http://sponsor.com</a></td></tr>
                    </tbody></table>
                </div>"""

TEST_ROWS_BLOCK = """<div class="block">
                    <h3 class="block_title">block title</h3>
                    <table class="rows_table">
                        <tbody>
                            <tr class="row_even">
                                <td colspan="1" valign="top">
                                    <div>row1</div>
                                </td>
                            </tr><tr class="row_odd">
                                <td colspan="1" valign="top">
                                    <div>row2</div>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>"""

TEST_TEXT_BLOCK = """<div class="block">
                    <h3 class="block_title">block title</h3>
                    <div class="block_text">text text text</div>
                </div>"""


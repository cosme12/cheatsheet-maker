"""Language selector handler

Todo:
    * Use internacionalization
    * Add more languages 
"""

english = {
    "INTRO_MESSAGE" : "Welcome to CheatSheet Maker",
    "MAIN_MENU_OPTIONS" : { 1: "Create sheet",
                            2: "Export (NOT CODED YET)",
                            3: "Help (NOT CODED YET)",
                            4: "Exit",
                            },
    "MENU_MESSAGE" : "Type the number to choose your option.",
    "CONFIG_SHEET_MESSAGE1" : "Building the basic layout... answer the next questions.",
    "CONFIG_SHEET_MESSAGE2" : "How many columns your sheet will have?",
    "CONFIG_SHEET_MESSAGE3" : "Which color style do you prefer?",
    "CONFIG_SHEET_OPTIONS1" : { 1: "What is your sheet title? ('CheatSheet' is added automatically)"
                            },
    "CONFIG_SHEET_OPTIONS2" : { 1: "1 main column",
                                2: "2 main columns",
                                3: "3 main columns"
                            },
    "CONFIG_SHEET_OPTIONS3" : { 1: "Orange",
                                2: "Black and white"
                            },
    "HEADER_MESSAGE" : "Building the header... answer the next questions.",
    "HEADER_OPTIONS" : { 1: "What is the author name?"
                        },
    "FOOTER_MESSAGE" : "Building the footer... answer the next questions.",
    "FOOTER_OPTIONS1" : { 1: "What is the author picture url?"
                        },
    "FOOTER_OPTIONS2" : { 1: "What is the author website url? (use http://)"
                        },
    "FOOTER_OPTIONS3" : { 1: "What is the sponsor name?"
                        },
    "FOOTER_OPTIONS4" : { 1: "What is the sponsor webite url? (use http://)"
                        },
    "BLOCK_MESSAGE" : "Building the blocks... answer the next questions.",
    "BLOCK_OPTIONS" : { 1: "Create text block",
                        2: "Create block with rows",
                        0: "Done"
                    },
    "BLOCK_ROWS_MESSAGE1" : "Building block with rows... answer the next questions.",
    "BLOCK_ROWS_MESSAGE2" : "In what main column do you want to build it?",
    "BLOCK_ROWS_OPTIONS1" : { 1: "What is the title of the block?"
                            },
    "BLOCK_ROWS_OPTIONS2" : { 1: "How many rows does it have?"
                            },
    "BLOCK_ROWS_OPTIONS3" : { 1: "What is the text of each row? (text row1. # text row2. # text row3)"
                            },
    "TEXT_BLOCK_MESSAGE" : "Building text block... answer the next questions.",
    "TEXT_BLOCK_EXTRA" : "main column",
    "TEXT_BLOCK_OPTIONS1" : { 1: "What is the title of the block?"
                            },
    "TEXT_BLOCK_OPTIONS2" : { 1: "What is the text for the block (use <br> for new line or any html tag for formatting)"
                            },
    "END_MESSAGE" : "Thanks for using CheatSheet Maker. Feel free to share your ideas at http://github.com/cosme12/cheasheet-maker",
    "EXIT_MESSAGE" : "Press any key to exit",
    "INVALID_INPUT_MESSAGE" : "Invalid input. Try again.",
}
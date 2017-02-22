"""Language selector handler

Todo:
    * Use internacionalization
    * Add more languages
"""

english = {
    "INTRO_MESSAGE": "Welcome to CheatSheet Maker",
    "MAIN_MENU_OPTIONS": {1: "Create sheet",
                          2: "Export (NOT CODED YET)",
                          3: "Help",
                          4: "Exit",
                          },
    "MENU_MESSAGE": "Type the number to choose your option.",
    "CONFIG_SHEET_MESSAGE1": "Building the basic layout... answer the next questions.",
    "CONFIG_SHEET_MESSAGE2": "How many columns your sheet will have?",
    "CONFIG_SHEET_MESSAGE3": "Which color style do you prefer?",
    "CONFIG_SHEET_OPTIONS1": {1: "What is your sheet title? ('CheatSheet' is added automatically)"
                              },
    "CONFIG_SHEET_OPTIONS2": {1: "1 main column",
                              2: "2 main columns",
                              3: "3 main columns"
                              },
    "CONFIG_SHEET_OPTIONS3" : { 1: "Orange",
                                2: "Black and white",
                                3: "Red",
                                4: "Yellow",
                                5: "Green",
                                6: "Blue",
                                },
    "HEADER_MESSAGE": "Building the header... answer the next questions.",
    "HEADER_OPTIONS": {1: "What is the author name?"
                        },
    "FOOTER_MESSAGE": "Building the footer... answer the next questions.",
    "FOOTER_OPTIONS1": {1: "What is the author picture url?"
                        },
    "FOOTER_OPTIONS2": {1: "What is the author website url? (use http://)"
                        },
    "FOOTER_OPTIONS3": {1: "What is the sponsor name?"
                        },
    "FOOTER_OPTIONS4": {1: "What is the sponsor webite url? (use http://)"
                        },
    "BLOCK_MESSAGE": "Building the blocks... answer the next questions.",
    "BLOCK_OPTIONS": {1: "Create text block",
                      2: "Create block with rows",
                      3: "Back to main menu"
                      },
    "BLOCK_ROWS_MESSAGE1": "Building block with rows... answer the next questions.",
    "BLOCK_ROWS_MESSAGE2": "In what main column do you want to build it?",
    "BLOCK_ROWS_OPTIONS1": {1: "What is the title of the block?"
                            },
    "BLOCK_ROWS_OPTIONS2": {1: "How many rows does it have?"
                            },
    "BLOCK_ROWS_OPTIONS3": {1: "What is the text of each row? (text row1. # text row2. # text row3)"
                            },
    "TEXT_BLOCK_MESSAGE": "Building text block... answer the next questions.",
    "TEXT_BLOCK_EXTRA": "main column",
    "TEXT_BLOCK_OPTIONS1": {1: "What is the title of the block?"
                            },
    "TEXT_BLOCK_OPTIONS2": {1: "What is the text for the block (use <br> for new line or any html tag for formatting)"
                            },
    "EXPORT_MESSAGE": "Select the correct option to export your file to pdf or png. (IMPORTANT: make sure you configure the exporter before doing anything).",
    "EXPORT_OPTIONS": {1: "Export to pdf",
                       2: "Export to png",
                       3: "Configure exporter",
                       4: "Back to main menu",
                      },
    "EXPORT_PDF": {1: "What is your file name? (ex: test)"
                  },
    "EXPORT_CONFIG": "In order to use the exporter you must download wkhtmltodpf. You can find it here: http://wkhtmltopdf.org/downloads.html\nAfter installation is done, write the path to the folder where it is.",
    "EXPORT_CONFIG_OPTIONS": {1: "What is the path to the folder where wkhtmltopdf is installed?"
                             },
    "EXPORT_ERROR": "You must configure exporter first. Make sure wkhtmltopdf is installed and the path is correct.",
    "END_MESSAGE": "Thanks for using CheatSheet Maker. Feel free to share your ideas at http://github.com/cosme12/cheasheet-maker",
    "EXIT_MESSAGE": "Press any key to exit",
    "INVALID_INPUT_MESSAGE": "Invalid input. Try again.",
}

espanol = {
    "INTRO_MESSAGE": "Bienvenido a CheatSheet Maker",
    "MAIN_MENU_OPTIONS": {1: "Crear hoja",
                          2: "Exportar (NOT CODED YET)",
                          3: "Ayuda",
                          4: "Salir",
                          },
    "MENU_MESSAGE": "Escribe el numero para elegir tu opcion",
    "CONFIG_SHEET_MESSAGE1": "Construyendo la estructura basica... responde las siguientes preguntas.",
    "CONFIG_SHEET_MESSAGE2": "Cuantas columnas tiene tu hoja?",
    "CONFIG_SHEET_MESSAGE3": "Que color de estilo prefieres?",
    "CONFIG_SHEET_OPTIONS1": {1: "Cual es el titulo de tu hoja? ('CheatSheet' se agrega automaticamente)"
                              },
    "CONFIG_SHEET_OPTIONS2": {1: "1 columna principal",
                              2: "2 columnas principales",
                              3: "3 columnas principales"
                              },
    "CONFIG_SHEET_OPTIONS3": {1: "Naranja",
                              2: "Negro y Blanco",
                              3: "Rojo",
                              4: "Amarillo",
                              5: "Verde",
                              6: "Azul",
                              },
    "HEADER_MESSAGE": "Construyendo el encabezado... responde las siguientes preguntas.",
    "HEADER_OPTIONS": {1: "Cual es el nombre del autor?"
                       },
    "FOOTER_MESSAGE": "Construyendo el pie de pagina... responde las siguientes preguntas.",
    "FOOTER_OPTIONS1": {1: "Cual es la url de la imagen del autor?"
                        },
    "FOOTER_OPTIONS2": {1: "Cual es la url del sitio web del autor? (use http://)"
                        },
    "FOOTER_OPTIONS3": {1: "Cual es el nombre del sponsor?"
                        },
    "FOOTER_OPTIONS4": {1: "Cual es la url del sitio web del sponsor? (use http://)"
                        },
    "BLOCK_MESSAGE": "Construyendo los bloques... responde las siguientes preguntas.",
    "BLOCK_OPTIONS": {1: "Crear bloque de texto",
                      2: "Crear bloque con filas",
                      3: "Volver al menu principal"
                      },
    "BLOCK_ROWS_MESSAGE1": "Construyendo bloque con filas... responde las siguientes preguntas.",
    "BLOCK_ROWS_MESSAGE2": "En que columna principal quieres construilo?",
    "BLOCK_ROWS_OPTIONS1": {1: "Cual es el titulo del bloque?"
                            },
    "BLOCK_ROWS_OPTIONS2": {1: "Cuantas filas tiene?"
                            },
    "BLOCK_ROWS_OPTIONS3": {1: "Cual es el texto de cada fila? (texto fila1. # texto fila2. # texto fila3.)"
                            },
    "TEXT_BLOCK_MESSAGE": "Construyendo bloque de texto... responde las siguientes preguntas.",
    "TEXT_BLOCK_EXTRA": "columna principal",
    "TEXT_BLOCK_OPTIONS1": {1: "Cual es el titulo del bloque?"
                            },
    "TEXT_BLOCK_OPTIONS2": {1: "Cual es el texto para el bloque? (usa <br> para nueva linea o cualquier html tag para dar formato)"
                            },
    "EXPORT_MESSAGE": "Selecciona la opcion correct para exportar tu hoja a pdf or png. (IMPORTANTE: asegurate de configurar el exportador antes de hacer cualquier otra cosa).",
    "EXPORT_OPTIONS": {1: "Exportar a pdf",
                       2: "Exportar a png",
                       3: "Configurar exportador",
                       4: "Volver al menu principal",
                      },
    "EXPORT_PDF": {1: "Cual es el nombre de tu archivo? (ej: prueba)"
                  },
    "EXPORT_CONFIG": "Para poder usar el exportador primero debes descargar wkhtmltodpf. Puedes encontrarlo aqui: http://wkhtmltopdf.org/downloads.html\nUna vez finalizada la instalacion escribe la ruta donde fue instalado.",
    "EXPORT_CONFIG_OPTIONS": {1: "Cual es la ruta a la carpeta donde wkhtmltopdf fue instalado?"
                             },
    "EXPORT_ERROR": "Primero debes configurar el exportador. Asegurate de que wkhtmltopdf esta instalado y que la ruta es correcta.",
    "END_MESSAGE": "Gracias por utilizar CheatSheet Maker. Comparte tus ideas en http://github.com/cosme12/cheasheet-maker",
    "EXIT_MESSAGE": "Presiona cualquier tecla para salir",
    "INVALID_INPUT_MESSAGE": "Entrada invalida. Pruba otra vez.",
}

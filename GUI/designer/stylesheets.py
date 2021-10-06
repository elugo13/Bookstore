
color1 = "#c4cddc"
color1mono = "#dce5f4"
color1mono_dark = "#c6d2e6"
color1_mono = "#afb9ca"
color1_mono2 = "#ffffff"
main_style_sheet = f"""
    QMainWindow {{
        background-color:{color1_mono};
    }}
    QPushButton {{
    font: 75 15pt "MS Sans Serif";
    background: {color1};
    color: white;
    border: 1px solid;
    border-radius: 2%;
   
    }}
    QPushButton:hover{{
    font: 75 15pt "MS Sans Serif";
    background: {color1mono};
    color: white;
    border: 1px solid;
    border-radius: 2%;
    }}
    QPushButton:hover:pressed{{
    font: 75 15pt "MS Sans Serif";
    background: {color1mono_dark};
    color: white;
    border: 1px solid;
    border-radius: 2%;
    }}
    QLabel {{
        font: 75 20pt "MS Sans Serif";
    }}
"""
dialog_style_sheet = f"""
QLabel#label{{
        font: 550 20pt "MS Sans Serif";
    }}
QLabel {{
        font: 550 13pt "MS Sans Serif";
    }}
QDialog {{
        background-color:{color1_mono2};

}}
"""

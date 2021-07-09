import string
from random import *
import PySimpleGUI as sg

# Choose a Theme for the Layout
sg.theme('DarkBlue')
# Create the window
layout = [[sg.Output(size=(20, 1), key='-OUTPUT-', font='Calibri 12', text_color='white')],
          [sg.Button('Generate Password', font='Calibri 12'), sg.Button('Clear', font='Calibri 12'),
           sg.Button('Exit', font='Calibri 12')]]
window = sg.Window("Password Generator", layout)


# Random string function
def passgen():
    characters = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(characters) for x in range(randint(8, 12)))
    print(password)


# Create an event loop
while True:
    event, values = window.read()
    # Generate a random string with letter, number and symbols
    # everytime the user presses the "Generate Password" button
    if event == "Generate Password":
        passgen()
        window['-OUTPUT-'].update('')
        passgen()
    # Delete the current password
    if event == 'Clear':
        window['-OUTPUT-'].update('')

    # End program if user closes window or
    # presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()

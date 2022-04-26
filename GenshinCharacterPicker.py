import PySimpleGUI as sg
import random

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Init empty character list
    characters = []

    # Check if file "CharacterArchive.txt" exists
    try:
        with open('CharacterArchive.txt', 'r') as file:
            # Read file and append each line to the character list
            for line in file:
                characters.append(line)
    except FileNotFoundError:
        # If file does not exist, create it
        with open('CharacterArchive.txt', 'w') as file:
            file.close()

    # Create a window
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Add characters to the list')],
              [sg.Text('Add a character'), sg.InputText()],
              [sg.Button('Add')],
              [sg.Text('Your characters')],
              [sg.Listbox(values=characters, size=(30, 10), key="characters")],
              [sg.Button('Delete')],
              [sg.Text('Generate random team')],
              [sg.Button('Randomize')],
              [sg.Text('', key='team')],
              ]

    # Create the Window
    window = sg.Window('Genshin Impact random team picker', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Add':
            # Add character to the list
            characters.append(values[0] + '\n')
            # Save to file
            with open('CharacterArchive.txt', 'a') as file:
                file.write(values[0] + '\n')
            # Update listbox
            window['characters'].Update(values=characters)
        if event == 'Randomize':
            if (len(characters) > 3):
                team = random.sample(characters, 4)
                teamString = ''
                for member in team:
                    teamString += member
                window['team'].Update(teamString)
        if event == 'Delete':
            # Delete character from the list
            deletedCharacter = window['characters'].get_indexes()
            if len(deletedCharacter) > 0:
                del characters[deletedCharacter[0]]
                # Save to file
                with open('CharacterArchive.txt', 'w') as file:
                    for character in characters:
                        file.write(character)
                # Update listbox
                window['characters'].Update(values=characters)

    window.close()




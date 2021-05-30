import PySimpleGUI as sg
from logbook_package import gen_win, gk, specs


'''
layout = [  [sg.Text("What's your name?'")],
            [sg.Input(key='-INPUT-')],
            [sg.Text('What is your favorite animal?')],
            [sg.Input(key='-INPUT2-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('New Window'), sg.Button('Quit')]
        ]

window = sg.Window('Testing PySimpleGUI', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Ok':
        if values['-INPUT2-'] == '' or values['-INPUT-'] == '':
            window['-OUTPUT-'].update('Please enter all fields.', text_color='red')
        else:
            window['-OUTPUT-'].update(f'Hello to {values["-INPUT-"]}! Your favorite animal is a {values["-INPUT2-"].lower()}',
                    text_color='white')
    elif event == 'New Window':
        window['-OUTPUT-'].update(f'Hmmm.....')
        new_layout = [  [sg.Text('Well this is awkward')]   ]
        new_window = sg.Window('New Window babyy!!!!', new_layout)
        new_event, new_values = new_window.read()

window.close()
'''

main_menu_window, log_a_jump_window = gen_win.generate_primary_window(), None
#REMOVE ME LATER
name = 'Kyle Hurd'
main_menu_window[gk._kGET_NAME_INPUT].update(f'Hello, {name}')

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED or event == gk._bQUIT:
        window.close()
        if window == log_a_jump_window:
            log_a_jump_window = None
        elif window == main_menu_window:
            break

    elif event == gk._bLAUNCH_LOG_JUMP_WINDOW and not log_a_jump_window: 
        # DELETE ME WHEN FUNCTIONALTY ADDED
        arr = ['Skydive Kapowsin', 'Caravan', 'Fusion 135']
        log_a_jump_window = gen_win.generate_log_a_jump_window(arr)

    elif event == gk._bVIEW_LOGBOOK:
        pass

    elif event == gk._bLOG_JUMP:
        logged_jump = specs.Logged_Jump()
        logged_jump.fill_logged_jump_from_dict(values)
        if logged_jump.verify_logged_jump():
            # NEED TO ADD DICT OR DATA STRUCT TO ADD A JUMP
            # DONT FORGET TO INCREMENT TOTAL_JUMPS
            # ALSO MAYBE CHECK TOTAL_JUMPS VS THE JUMP# OF NEW JUMP??
            pass



import PySimpleGUI as sg
from datetime import date
import logbook_package.global_keys as gk

def generate_primary_window() -> sg.Window:
    '''
    Generates the main menu window to navigate pages.

    :rtype sg.Window(): GUI Window for main page
    '''

    layout_column = [
                [sg.Text(f'Hello, NAME REDACTED', key=gk._kGET_NAME_INPUT, pad=(0,50))],
                [sg.Button(gk._bLAUNCH_LOG_JUMP_WINDOW, pad=(0,15))],
                [sg.Button(gk._bVIEW_LOGBOOK, pad=(0,15))],
                [sg.Button(gk._bQUIT, pad=(0,15))]
            ]

    layout = [
                [sg.Column(layout_column, justification='c', element_justification='center')]
            ]

    return (sg.Window('Main Menu', layout,
            size=(300,400), grab_anywhere=True, finalize=True)
            )


def generate_log_a_jump_window(skydiver_default_info: list[str]) -> sg.Window:
    '''
    Generates GUI window to log a jump.

    :param skydiver_default_info list[str]: [0] - Default Location,
                                            [1] - Default Aircraft,
                                            [2] - Default Equipment,
    :rtype sg.Window(): GUI Window for logging jump
    '''

    today: str = date.today().strftime('%m/%d/%Y')
    
    log_button_to_be_centered = [[sg.Button(gk._bLOG_JUMP)]]
    layout = [
                [sg.Text('Jump #: N/A', key=gk._kUPDATE_JUMP_NUMBER, size=(20,1), pad=(0,20))],

                [sg.Text('Date:', size=(20,1)), sg.Input(default_text=today,
                    key=gk._kGET_DATE_OF_JUMP_INPUT)],

                [sg.Text('Exit Altitude:', size=(20,1)), sg.Input(default_text='13000',
                   key=gk._kGET_EXIT_ALTITUDE_INPUT)],

                [sg.Text('Location:', size=(20,1)), sg.Input(default_text=skydiver_default_info[0],
                   key=gk._kGET_DROP_ZONE_LOCATION_INPUT)],

                [sg.Text('Aircraft:', size=(20,1)), sg.Input(default_text=skydiver_default_info[1],
                   key=gk._kGET_AIRCRAFT_INPUT)],

                [sg.Text('Equipment:', size=(20,1)), sg.Input(default_text=skydiver_default_info[2],
                   key=gk._kGET_PARACHUTE_MODEL_SIZE_INPUT)],

                [sg.Text('Signature:', size=(20,1)), sg.Input(key=gk._kGET_SIGNATURE_INPUT)],
                
                [sg.Text('Description:', size=(20,1)), sg.Multiline(key=gk._kGET_DESCRIPTION_OF_JUMP)],

                [sg.Column(log_button_to_be_centered, justification='c', element_justification='center')]
            ]

    return (sg.Window('Log A Jump', layout,
            grab_anywhere=True, finalize=True)
            )


def generate_create_new_logbook_window(skydiver_default_info: list[str]) -> sg.Window:
    '''
    GUI to create a new logbook if a .csv file containing jumps is not found.

    :param skydiver_default_info list[str]: Skydiver's default information.
    :rtype sg.Window: The GUI Window
    '''
     
    today: str = date.today().strftime('%m/%d/%Y')
    
    log_button_to_be_centered = [[sg.Button(gk._bLOG_JUMP), sg.Button(gk._bQUIT)]]
    layout = [
                [sg.Text("It appears you do not have a log book set up. Let's get that set up!", key='-UPDATE_TEXT-')],

                [sg.Text('Jump #:', size=(20,1)), sg.Input(key=gk._kGET_JUMP_NUMBER)],

                [sg.Text('Date:', size=(20,1)), sg.Input(default_text=today,
                    key=gk._kGET_DATE_OF_JUMP_INPUT)],

                [sg.Text('Exit Altitude:', size=(20,1)), sg.Input(default_text='13000',
                   key=gk._kGET_EXIT_ALTITUDE_INPUT)],

                [sg.Text('Location:', size=(20,1)), sg.Input(default_text=skydiver_default_info[0],
                   key=gk._kGET_DROP_ZONE_LOCATION_INPUT)],

                [sg.Text('Aircraft:', size=(20,1)), sg.Input(default_text=skydiver_default_info[1],
                   key=gk._kGET_AIRCRAFT_INPUT)],

                [sg.Text('Equipment:', size=(20,1)), sg.Input(default_text=skydiver_default_info[2],
                   key=gk._kGET_PARACHUTE_MODEL_SIZE_INPUT)],

                [sg.Text('Signature:', size=(20,1)), sg.Input(key=gk._kGET_SIGNATURE_INPUT)],
                
                [sg.Text('Description:', size=(20,1)), sg.Multiline(key=gk._kGET_DESCRIPTION_OF_JUMP)],

                [sg.Column(log_button_to_be_centered, justification='c', element_justification='center')]
            ]

    return (sg.Window('First Log', layout,
            grab_anywhere=True, finalize=True)
            )


def generate_view_log_book_window() -> sg.Window:
    pass

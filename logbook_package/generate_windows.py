import PySimpleGUI as sg
from datetime import date

import logbook_package.global_keys as gk
import logbook_package.skydiver_info as specs
import logbook_package.parser as parser


def generate_primary_window() -> sg.Window:
    '''
    Generates the main menu window to navigate pages.

    :rtype sg.Window(): GUI Window for main page
    '''

    layout_column = [
                [sg.Text('Hello, <INSERT_NAME>', key=gk._kGET_NAME_INPUT, pad=(0,50))],
                [sg.Button(gk._bLAUNCH_LOG_JUMP_WINDOW, pad=(0,15))],
                [sg.Button(gk._bVIEW_LOGBOOK, pad=(0,15))],
                [sg.Button(gk._bQUIT, pad=(0,15))]
            ]

    layout = [
                [sg.Column(layout_column, justification='c', element_justification='center')]
            ]

    return sg.Window('Main Menu', layout, size=(300,400), finalize=True)


def generate_log_a_jump_window(skydiver_default_info: list[str]) -> sg.Window:
    '''
    Generates GUI window to log a jump.

    :param skydiver_default_info list[str]: [0] - Default Location,
                                            [1] - Default Aircraft,
                                            [2] - Default Equipment,
    :rtype sg.Window(): GUI Window for logging jump
    '''

    today: str = date.today().strftime('%m/%d/%Y')
    
    log_button_to_be_centered = [[sg.Button(gk._bLOG_JUMP), sg.Button(gk._bEXIT)]]
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

    return sg.Window('Log A Jump', layout, finalize=True)


def generate_create_new_logbook_window(skydiver_default_info: list[str]) -> sg.Window:
    '''
    GUI to create a new logbook if a .csv file containing jumps is not found.

    :param skydiver_default_info list[str]: Skydiver's default information.
    :rtype sg.Window: The GUI Window
    '''
     
    today: str = date.today().strftime('%m/%d/%Y')
    
    log_button_to_be_centered = [[sg.Button(gk._bLOG_JUMP), sg.Button(gk._bEXIT)]]
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
    
    return sg.Window('First Log', layout, finalize=True)


def generate_view_log_book_window(
        default_skydiver_info: specs.Skydiver_Personal_Info,
        logbook: list[specs.Logged_Jump]
        ) -> sg.Window:
    
    # Renaming Function to add multiple spaces to string
    space = parser.space


    jumps_list = parser.parse_logbook_to_string(logbook)

    title = ('Jump #' + space(3) +
            'Date' + space(15) +
            'Location' + space(18) +
            'Aircraft' + space(15) +
            'Exit Altitude' + space(3) +
            'Equipment' + space(10) +
            'Signature' + space(15) +
            'Description' + space(15)
            )


    layout = [
            [ sg.Frame('Logbook', layout=[[sg.Text(title)]])],
            [ sg.Listbox(values=jumps_list, size=(150,18), key=gk._kUPDATE_VIEW_LOG_BOOK_LIST)],
            [ sg.Button(gk._bEXIT)]
            ]

    return sg.Window('View Logbook', layout, finalize=True)


# CONTROLLERS

def create_new_logbook(
        default_skydiver_info: specs.Skydiver_Personal_Info,
        logbook: list[specs.Logged_Jump]
        ) -> None:
    '''
    Generates GUI window to log a new jump and creates a new logbook if one is not found.

    :param default_skydiver_info specs.Skydiver_Personal_Info: Personal information on the skydiver.
    :param logbook list[specs.Logged_Jump]: The logbook to be used. Logbook list needs to be empty.
    :rtype None:
    '''

    create_new_logbook_window = generate_create_new_logbook_window(
            [
                    default_skydiver_info.current_dropzone,
                    default_skydiver_info.primary_aircraft,
                    default_skydiver_info.parachute_model + ' ' + default_skydiver_info.parachute_size
                    ]
                )

    logged_jump = specs.Logged_Jump()

    while True:

        event, values = create_new_logbook_window.read()
        
        if event == sg.WINDOW_CLOSED or event == gk._bEXIT:

            create_new_logbook_window.close()
            sys.exit('No logged jump or logbook.')

        elif event == gk._bLOG_JUMP:

            logged_jump.fill_logged_jump_from_dict(values)

            if logged_jump.verify_logged_jump():
                logbook.insert(0, logged_jump)
                create_new_logbook_window.close()
                break

            else:
                create_new_logbook_window.Element('-UPDATE_TEXT-').update('Please enter information into ALL fields.', background_color='red')

    return None


def create_home_page(
        default_skydiver_info: specs.Skydiver_Personal_Info,
        logbook: list[specs.Logged_Jump]
        ) -> None:
    
    main_menu_window, log_a_jump_window, view_log_book_window = generate_primary_window(), None, None
    main_menu_window[gk._kGET_NAME_INPUT].update(f'Hello, {default_skydiver_info.name}')


    while True:
        window, event, values = sg.read_all_windows()

        if event == sg.WINDOW_CLOSED or event == gk._bQUIT or event == gk._bEXIT:
            window.close()
            if window == log_a_jump_window:
                log_a_jump_window = None

            elif window == view_log_book_window:
                view_log_book_window = None

            elif window == main_menu_window:
                break

        elif event == gk._bLAUNCH_LOG_JUMP_WINDOW and not log_a_jump_window:

            arr = [
                    default_skydiver_info.current_dropzone,
                    default_skydiver_info.primary_aircraft,
                    default_skydiver_info.parachute_model + ' ' + default_skydiver_info.parachute_size
                ]
            log_a_jump_window = generate_log_a_jump_window(arr)
            log_a_jump_window[gk._kUPDATE_JUMP_NUMBER].update(f'Jump #: {int(logbook[-1].jump_number) + 1}')

        elif event == gk._bVIEW_LOGBOOK:

            view_log_book_window = generate_view_log_book_window(default_skydiver_info, logbook)

        elif event == gk._bLOG_JUMP and log_a_jump_window:

            values[gk._kGET_JUMP_NUMBER] = int(logbook[-1].jump_number) + 1

            logged_jump = specs.Logged_Jump()
            logged_jump.fill_logged_jump_from_dict(values)

            if logged_jump.verify_logged_jump():

                logbook.insert(len(logbook), logged_jump)
                parser.save_logbook(logbook, gk._fLOGBOOK_CSV)

                if view_log_book_window != None:
                    view_log_book_window[gk._kUPDATE_VIEW_LOG_BOOK_LIST].update(parser.parse_logbook_to_string(logbook))

                log_a_jump_window.close()
                log_a_jump_window = None

            else:
                log_a_jump_window[gk._kUPDATE_JUMP_NUMBER].update('Please enter in all fields', background_color='red')

    return None

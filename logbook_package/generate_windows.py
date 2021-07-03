import PySimpleGUI as sg
from datetime import date
import csv

import logbook_package.global_keys as gk
import logbook_package.skydiver_info as specs
import logbook_package.parser as parser


def generate_primary_window(specs: specs.Skydiver_Personal_Info, logbook: list[specs.Logged_Jump]) -> sg.Window:
    '''
    Generates the main menu window to navigate pages.

    :rtype sg.Window(): GUI Window for main page
    '''

    btn_pad = (40,15)
    btn_layout = [
            [ sg.Button(gk._bLAUNCH_LOG_JUMP_WINDOW, pad=btn_pad),
                sg.Button(gk._bVIEW_LOGBOOK, pad=btn_pad),
                sg.Button(gk._bQUIT, pad=btn_pad)]
            ]


    specs_text = [
            [ sg.Text(f'Name:             {specs.name}') ],
            [ sg.Text(f'License #:        {specs.license_number}') ],
            [ sg.Text(f'# Jumps:          {logbook[-1].jump_number}')],
            [ sg.Text(f'Current DZ:       {specs.current_dropzone}') ],
            [ sg.Text(f'Equipment:        {specs.parachute_brand} {specs.parachute_model} {specs.parachute_size}')],
            [ sg.Text(f'Primary Aircraft: {specs.primary_aircraft}') ]
            ]


    layout = [
            [ sg.Frame(f"{specs.name}'s Logbook", layout=specs_text), sg.Image('./static/images/skydiver.png') ],
            # [ sg.Image('./static/images/skydiver.png') ],
            [ sg.Column(btn_layout, justification='r', element_justification='right') ]
            ]

    return sg.Window('Main Menu', layout, finalize=True, font=('Helvetica', 12))


def generate_log_a_jump_window(skydiver_default_info: list[str]) -> sg.Window:
    '''
    Generates GUI window to log a jump.

    :param skydiver_default_info list[str]: [0] - Default Location,
                                            [1] - Default Aircraft,
                                            [2] - Default Equipment,
    :rtype sg.Window(): GUI Window for logging jump
    '''

    today: str = date.today().strftime('%m/%d/%Y')
    size_v = (20,1)
    
    log_button_to_be_centered = [[sg.Button(gk._bLOG_JUMP), sg.Button(gk._bBACK)]]
    layout = [
                [sg.Text('Jump #: N/A', key=gk._kUPDATE_JUMP_NUMBER, size=size_v, pad=(0,20))],

                [sg.Text('Date:', size=size_v), sg.Input(default_text=today,
                    key=gk._kGET_DATE_OF_JUMP_INPUT)],

                [sg.Text('Exit Altitude:', size=size_v), sg.Input(default_text='13000',
                   key=gk._kGET_EXIT_ALTITUDE_INPUT)],

                [sg.Text('Location:', size=size_v), sg.Input(default_text=skydiver_default_info[0],
                   key=gk._kGET_DROP_ZONE_LOCATION_INPUT)],

                [sg.Text('Aircraft:', size=size_v), sg.Input(default_text=skydiver_default_info[1],
                   key=gk._kGET_AIRCRAFT_INPUT)],

                [sg.Text('Equipment:', size=size_v), sg.Input(default_text=skydiver_default_info[2],
                   key=gk._kGET_PARACHUTE_MODEL_SIZE_INPUT)],

                [sg.Text('Signature:', size=size_v), sg.Input(key=gk._kGET_SIGNATURE_INPUT)],
                
                [sg.Text('Description:', size=size_v), sg.Multiline(key=gk._kGET_DESCRIPTION_OF_JUMP)],

                [sg.Column(log_button_to_be_centered, justification='c', element_justification='center')]
            ]

    return sg.Window('Log A Jump', layout, finalize=True, font=('Helvetica', 12))


def generate_create_new_logbook_window(skydiver_default_info: list[str]) -> sg.Window:
    '''
    GUI to create a new logbook if a .csv file containing jumps is not found.

    :param skydiver_default_info list[str]: Skydiver's default information.
    :rtype sg.Window: The GUI Window
    '''
     
    today: str = date.today().strftime('%m/%d/%Y')
    size_v = (20,1)
    
    log_button_to_be_centered = [[sg.Button(gk._bLOG_JUMP), sg.Button(gk._bEXIT)]]
    layout = [
                [sg.Text("It appears you do not have a log book set up. Let's get that set up!", key='-UPDATE_TEXT-')],

                [sg.Text('Jump #:', size=size_v), sg.Input(key=gk._kGET_JUMP_NUMBER)],

                [sg.Text('Date:', size=size_v), sg.Input(default_text=today,
                    key=gk._kGET_DATE_OF_JUMP_INPUT)],

                [sg.Text('Exit Altitude:', size=size_v), sg.Input(default_text='13000',
                   key=gk._kGET_EXIT_ALTITUDE_INPUT)],

                [sg.Text('Location:', size=size_v), sg.Input(default_text=skydiver_default_info[0],
                   key=gk._kGET_DROP_ZONE_LOCATION_INPUT)],

                [sg.Text('Aircraft:', size=size_v), sg.Input(default_text=skydiver_default_info[1],
                   key=gk._kGET_AIRCRAFT_INPUT)],

                [sg.Text('Equipment:', size=size_v), sg.Input(default_text=skydiver_default_info[2],
                   key=gk._kGET_PARACHUTE_MODEL_SIZE_INPUT)],

                [sg.Text('Signature:', size=size_v), sg.Input(key=gk._kGET_SIGNATURE_INPUT)],
                
                [sg.Text('Description:', size=size_v), sg.Multiline(key=gk._kGET_DESCRIPTION_OF_JUMP)],

                [sg.Column(log_button_to_be_centered, justification='c', element_justification='center')]
            ]
    
    return sg.Window('First Log', layout, finalize=True, font=('Helvetica', 12))


def generate_view_log_book_window(
        default_skydiver_info: specs.Skydiver_Personal_Info,
        logbook: list[specs.Logged_Jump]
        ) -> sg.Window:
    '''
    Generates a viewable form of the logged jumps.

    :param default_skydiver_info specs.Skydiver_Personal_Info: Personal information regarding the skydiver.
    :param logbook list[specs.Logged_Jump]: The jump information of the jumper.
    :rtype sg.Window: The GUI to be viewed by the user.
    '''

    header_list = ['Jump No.','Date','Exit Altitude','Location','Aircraft','Equipment','Signature','Description']
    data = [[j.jump_number, j.date, j.exit_altitude, j.location, j.aircraft, j.equipment, j.signature, j.description] for j in logbook]
    text = [[sg.Text(f'# Jumps:   {logbook[-1].jump_number}'),
            sg.Text(f'Equipment: {default_skydiver_info.parachute_brand} {default_skydiver_info.parachute_model} {default_skydiver_info.parachute_size}')]]

    title = [sg.Frame(f"{default_skydiver_info.name}'s Logbook", layout=text)]
    edit_btn = [[sg.Button(button_text=gk._bGET_TABLE), sg.Button(button_text=gk._bBACK)]]

    layout = [

            [title],

            [
                sg.Table(
                    values=data,
                    headings=header_list,
                    max_col_width=25,
                    auto_size_columns=True,
                    justification='left',
                    alternating_row_color='black',
                    key=gk._kGET_TABLE,
                    select_mode=sg.TABLE_SELECT_MODE_BROWSE
                    )
                ],

            [sg.Column(edit_btn, justification='c', element_justification='ceneter')]

            ]

    return sg.Window('View Logbook', layout, finalize=True, font=('Helvetica', 12))


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
    
    main_menu_window, log_a_jump_window, view_log_book_window = generate_primary_window(default_skydiver_info, logbook), None, None

    while True:

        window, event, values = sg.read_all_windows()
        
        if event in (sg.WINDOW_CLOSED, gk._bQUIT, gk._bEXIT, gk._bBACK):

            if window != None:
                window.close()

            if window in (log_a_jump_window, view_log_book_window):
                main_menu_window = generate_primary_window(default_skydiver_info, logbook)

            elif window == main_menu_window:
                break

        elif event == gk._bLAUNCH_LOG_JUMP_WINDOW:

            main_menu_window.close()
            arr = [
                    default_skydiver_info.current_dropzone,
                    default_skydiver_info.primary_aircraft,
                    default_skydiver_info.parachute_model + ' ' + default_skydiver_info.parachute_size
                ]
            log_a_jump_window = generate_log_a_jump_window(arr)
            log_a_jump_window[gk._kUPDATE_JUMP_NUMBER].update(f'Jump #: {int(logbook[-1].jump_number) + 1}')
       
        # A SUBSET OF THE VIEW LOGBOOK WINDOW
        elif event == gk._bGET_TABLE:
            logged_jump = values[gk._kGET_TABLE]
            # FIGURE OUT A NICE WAY TO EDIT EXISTING JUMPS. MAYBE TRY TO UPDATE THE PAGE? OR JUST GENERATE NEW ONE

        elif event == gk._bVIEW_LOGBOOK:

            main_menu_window.close()
            view_log_book_window = generate_view_log_book_window(default_skydiver_info, logbook)

        elif event == gk._bLOG_JUMP:

            values[gk._kGET_JUMP_NUMBER] = int(logbook[-1].jump_number) + 1

            logged_jump = specs.Logged_Jump()
            logged_jump.fill_logged_jump_from_dict(values)

            if logged_jump.verify_logged_jump():

                logbook.insert(len(logbook), logged_jump)
                parser.save_logbook(logbook, gk._fLOGBOOK_CSV)

                log_a_jump_window.close()
                main_menu_window = generate_primary_window(default_skydiver_info, logbook)

            else:
                log_a_jump_window[gk._kUPDATE_JUMP_NUMBER].update('Please enter in all fields', background_color='red')

    return None

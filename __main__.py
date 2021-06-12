import PySimpleGUI as sg
from logbook_package import gen_win, gk, specs, parser

# Grab the last jump no. logged in the csv, file, this will be the total amount of jumps. Use this to
# track the total num of jumps

# If the csv is empty, let them log the next jump num and start there
sg.theme('Purple')
default_skydiver_info: specs.Skydiver_Personal_Info = parser.parse_skydiver_info_file(gk._fSKYDIVER_INFO_TXT)
logbook: list[specs.Logged_Jump] = parser.parse_logbook_csv(gk._fLOGBOOK_CSV)

if len(logbook) == 0:
    # MAKE A FUNCTION INSIDE GENERATE_WINDOWS TO CREATE A WINDOW AND 
    # TO GENERATE A WINDOW TO LOG THE FIRST JUMP
    create_new_logbook_window = gen_win.generate_create_new_logbook_window(
            [
                    default_skydiver_info.current_dropzone,
                    default_skydiver_info.primary_aircraft,
                    default_skydiver_info.parachute_model + ' ' + default_skydiver_info.parachute_size
                    ]
                )

    logged_jump = specs.Logged_Jump()

    while True:
        event, values = create_new_logbook_window.read()
        
        if event == sg.WINDOW_CLOSED or event == gk._bQUIT:
            create_new_logbook_window.close()
            exit()

        elif event == gk._bLOG_JUMP:
            logged_jump.fill_logged_jump_from_dict(values)
            if logged_jump.verify_logged_jump():
                logbook.insert(0, logged_jump)
                break
            else:
                create_new_logbook_window.Element('-UPDATE_TEXT-').update('Please enter information into ALL fields.', background_color='red')


# NEXT BLOCK

main_menu_window, log_a_jump_window = gen_win.generate_primary_window(), None
main_menu_window[gk._kGET_NAME_INPUT].update(f'Hello, {default_skydiver_info.name}')


while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED or event == gk._bQUIT:
        window.close()
        if window == log_a_jump_window:
            log_a_jump_window = None
        elif window == main_menu_window:
            break

    elif event == gk._bLAUNCH_LOG_JUMP_WINDOW and not log_a_jump_window:

        arr = [
                default_skydiver_info.current_dropzone,
                default_skydiver_info.primary_aircraft,
                default_skydiver_info.parachute_model + ' ' + default_skydiver_info.parachute_size
            ]
        log_a_jump_window = gen_win.generate_log_a_jump_window(arr)
        log_a_jump_window[gk._kUPDATE_JUMP_NUMBER].update(f'Jump #: {len(logbook) + 1}')

    elif event == gk._bVIEW_LOGBOOK:
        pass

    elif event == gk._bLOG_JUMP:

        logged_jump = specs.Logged_Jump()
        logged_jump.fill_logged_jump_from_dict(values)

        if logged_jump.verify_logged_jump():
            logbook.insert(0, logged_jump)
            pass

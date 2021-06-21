import logbook_package.global_keys as gk
import logbook_package.skydiver_info as specs
import csv

def parse_skydiver_info_file(filename: str) -> specs.Skydiver_Personal_Info:
    '''
    Grabs skydiver information from .txt format and converts it to Skydiver_Personal_Info -like struct

    :param filename str: Path to the .txt file to read
    :rtype specs.Skydiver_Personal_Info: Struct-like class storing the user's stats'
    '''
        
    skydiver_info: dict = {}
    
    with open(filename, 'r') as _:

        for line in _:
            logged_info = line.split(':', 1)
            logged_info[0] = logged_info[0].strip()
            logged_info[1] = logged_info[1].strip()
            skydiver_info[logged_info[0]] = logged_info[1]
    
    info = specs.Skydiver_Personal_Info()
    info.name = skydiver_info[gk._dNAME]
    info.parachute_brand = skydiver_info[gk._dPARACHUTE_BRAND]
    info.parachute_model = skydiver_info[gk._dPARACHUTE_MODEL]
    info.parachute_size = skydiver_info[gk._dPARACHUTE_SIZE]
    info.current_dropzone = skydiver_info[gk._dCURRENT_DROPZONE]
    info.primary_aircraft = skydiver_info[gk._dPRIMARY_AIRCRAFT]

    return info


def parse_logbook_csv(filename: str) -> list[specs.Logged_Jump]:
    '''
    Parses jumps logged in csv. The first line must be the titles and will be deleted.

    :param filename str: Location to the .csv file to read
    :rtype list[specs.Logged_Jump]: A list of each logged jump within .csv
    '''
    
    logbook: list = []

    with open(filename, 'r') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        
        for row in csv_reader:
            temp = specs.Logged_Jump()
            temp.jump_number = row[0]
            temp.date = row[1]
            temp.exit_altitude = row[2]
            temp.location = row[3]
            temp.aircraft = row[4]
            temp.equipment = row[5]
            temp.signature = row[6]
            temp.description = row[7]
            logbook.append(temp)


    if len(logbook) != 0:
        logbook.pop(0) # Remove the titles/first line

    return logbook


def save_logbook(logbook: list[specs.Logged_Jump], outfile: str) -> None:
    '''
    Rewrites logbook csv to contain all contents of the logbook passed in.

    :param logbook list[specs.Logged_Jump]: The list of jumps to overwrite the logbook csv file
    :rtype None:
    '''

    with open(outfile, 'w') as f_:
        print('Jump No.,Date,Exit Altitude,Location,Aircraft,Equipment,Signature,Description', file=f)
        for jump in logbook:
            print(f'{jump.jump_number},{jump.date},{jump.exit_altitude},{jump.location},' \
                    f'{jump.aircraft},{jump.equipment},{jump.signature},{jump.description}', file=f_)

    return None


def space(offset: int) -> str:
    '''
    Creates a string of 'offset' number of spaces.

    :param offset int: The number of spaces to be in the string
    :rtype str: 'offset' number of spaces
    '''
    return ' ' * offset


def parse_logbook_to_string(logbook: list[specs.Logged_Jump]) -> list[str]:
    '''
    Converts list of Logged_Jump() to list of str for ease of display in a GUI.

    :param logbook list[specs.Logged_Jump]: The list of all logged jumps to be displayed
    :rtype list[str]: Converted list of all logged jumps to be displayed
    '''

    return ([
            f'{logbook[i].jump_number[0:12]:<13s}{logbook[i].date[0:14]:<15s}' \
                    f'{logbook[i].location[0:19]:<20s}{logbook[i].aircraft[0:19]:<20s}' \
                    f'{logbook[i].exit_altitude[0:14]:<15s}' \
                    f'{logbook[i].equipment[0:19]:<20s}{logbook[i].signature[0:19]:<20s}' \
                    f'{logbook[i].description[0:75]:<25s}' for i in range(len(logbook))
                    ])

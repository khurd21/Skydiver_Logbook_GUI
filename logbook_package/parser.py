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

    logbook.pop(0) # Remove the titles/first line

    return logbook

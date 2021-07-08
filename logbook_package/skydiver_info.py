import datetime as dt
import logbook_package.global_keys as gk


class Skydiver_Personal_Info:
    '''A struct-like class to hold statistics of the jumper'''
    
    def __init__(self):
        self.name: str = ''
        self.parachute_brand: str = ''
        self.parachute_model: str = ''
        self.parachute_size: str = ''
        self.current_dropzone: str = ''
        self.primary_aircraft: str = ''
        self.license_number: str = ''
        return




class Logged_Jump:
    '''Stores information regarding a singly logged jump.'''

    def __init__(self):
        self.date: str = ''
        self.exit_altitude: str = ''
        self.location: str = ''
        self.aircraft: str = ''
        self.equipment: str = ''
        self.signature: str = ''
        self.description: str = ''
        self.jump_number: str = ''
        return


    def __lt__(self, rhs) -> bool:
        date_format: str = '%m/%d/%Y'
        dt_rhs = dt.datetime.strptime(rhs.date, date_format)
        dt_lhs = dt.datetime.strptime(self.date, date_format)
        return dt_lhs < dt_rhs


    def _verify_date(self) -> bool:
        '''
        Checks if the date provided is in the mm/dd/yyyy format.

        :rtype bool: True if in mm/dd/yyyy format, false otherwise]
        '''

        correct_format: str = '%m/%d/%Y'
        state: bool = False

        try:
            dt.datetime.strptime(self.date, correct_format)
            state = True

        except ValueError:
            state = False

        return state

    
    def _verify_exit_altitude(self) -> bool:
        '''
        Checks if a string is provided for the var 'exit_altitude' and
        if the string can be represented as an integer (eg. '12' -> 12)

        :rtype bool: True if exit_altitude is a digit and not empty, False otherwise
        '''
        return self.exit_altitude.isdigit() and self.exit_altitude != ''


    def _verify_location(self) -> bool:
        return self.location != ''


    def _verify_aircraft(self) -> bool:
        return self.aircraft != '' 


    def _verify_equipment(self) -> bool:
        return self.equipment != ''


    def _verify_signature(self) -> bool:
        return self.signature != ''


    def _verify_description(self) -> bool:
        return self.description != ''


    def _verify_jump_number(self) -> bool:
        return self.jump_number.isdigit() and self.jump_number != ''


    def verify_logged_jump(self) -> bool:
        return (
                self._verify_equipment() and
                self._verify_exit_altitude() and
                self._verify_date() and
                self._verify_aircraft() and
                self._verify_location() and
                self._verify_description()
                )
    

    def update_jump_number(self, jump_no: int) -> None:
        self.jump_number = jump_no
        return None


    def fill_logged_jump_from_dict(self, values: dict) -> None:
        '''
        Grabs values from dictionary pulled from the GUI to assign to class variables.

        :param values dict: The values collected from GUI
        :rtype None: 
        '''

        self.aircraft = str(values[gk._kGET_AIRCRAFT_INPUT].strip())
        self.date = str(values[gk._kGET_DATE_OF_JUMP_INPUT].strip())
        self.description = str(values[gk._kGET_DESCRIPTION_OF_JUMP].strip())
        self.signature = str(values[gk._kGET_SIGNATURE_INPUT].strip())
        self.equipment = str(values[gk._kGET_PARACHUTE_MODEL_SIZE_INPUT].strip())
        self.exit_altitude = str(str(values[gk._kGET_EXIT_ALTITUDE_INPUT].strip()))
        self.jump_number = str(values[gk._kGET_JUMP_NUMBER])
        self.location = str(values[gk._kGET_DROP_ZONE_LOCATION_INPUT].strip())

        return None

import datetime as dt
import logbook_package.global_keys as gk


class Skydiver_Personal_Info:
    
    def __init__(self):
        self.name: str = ''
        self.parachute_brand: str = ''
        self.parachute_model: str = ''
        self.parachute_size: str = ''
        self.current_dropzone: str = ''
        self.primary_aircraft: str = ''
        self.total_number_of_jumps: int = 0
        return




class Logged_Jump:

    def __init__(self):
        self.date: str = ''
        self.exit_altitude: str = ''
        self.location: str = ''
        self.aircraft: str = ''
        self.equipment: str = ''
        self.description: str = ''
        self.jump_number: int = 0
        return


    def _verify_date(self) -> bool:

        correct_format: str = '%m/%d/%Y'
        state: bool = False

        try:
            dt.datetime.strptime(self.date, correct_format)
            state = True

        except ValueError:
            state = False

        return state

    
    def _verify_exit_altitude(self) -> bool:
        return self.exit_altitude.isdigit() and self.exit_altitude != ''


    def _verify_location(self) -> bool:
        return self.location != ''


    def _verify_aircraft(self) -> bool:
        return self.aircraft != '' 


    def _verify_equipment(self) -> bool:
        return self.equipment != ''


    def _verify_description(self) -> bool:
        return self.description != ''


    def verify_logged_jump(self) -> bool:
        return (
                _verify_equipment and
                _verify_exit_altitude and
                _verify_date and
                _verify_aircraft and
                _verify_location and
                _verify_description
                )

    def fill_logged_jump_from_dict(self, values: dict) -> None:
        self.aircraft = values[gk._kGET_AIRCRAFT_INPUT]
        self.date = values[gk._kGET_DATE_OF_JUMP_INPUT]
        self.description = values[gk._kGET_DESCRIPTION_OF_JUMP]
        self.equipment = values[gk._kGET_PARACHUTE_MODEL_SIZE_INPUT]
        self.exit_altitude = values[gk._kGET_EXIT_ALTITUDE_INPUT]
        self.jump_number = values[gk._kGET_JUMP_NUMBER]
        self.location = values[gk._kGET_DROP_ZONE_LOCATION_INPUT]
        return None

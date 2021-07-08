import PySimpleGUI as sg
from logbook_package import gen_win, gk, specs, parser


default_skydiver_info: specs.Skydiver_Personal_Info = parser.parse_skydiver_info_file(gk._fSKYDIVER_INFO_TXT)
logbook: list[specs.Logged_Jump] = parser.parse_logbook_csv(gk._fLOGBOOK_CSV)

if len(logbook) == 0:
    gen_win.create_new_logbook(default_skydiver_info, logbook)

first_jump_no = int(logbook[0].jump_number)
gen_win.create_home_page(default_skydiver_info, logbook)

logbook.sort()
for i, log in enumerate(logbook):
    log.jump_number = i + first_jump_no 

parser.save_logbook(logbook, gk._fLOGBOOK_CSV)

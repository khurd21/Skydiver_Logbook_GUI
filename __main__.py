import PySimpleGUI as sg
import sys
from logbook_package import gen_win, gk, specs, parser


default_skydiver_info: specs.Skydiver_Personal_Info = parser.parse_skydiver_info_file(gk._fSKYDIVER_INFO_TXT)
logbook: list[specs.Logged_Jump] = parser.parse_logbook_csv(gk._fLOGBOOK_CSV)

if len(logbook) == 0:
    gen_win.create_new_logbook(default_skydiver_info, logbook)

gen_win.create_home_page(default_skydiver_info, logbook)
parser.save_logbook(logbook, gk._fLOGBOOK_CSV)

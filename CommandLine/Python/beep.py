import argparse, winsound
parser = argparse.ArgumentParser()
# parser.add_argument("beep", choices=["ASTERISK", "EXCLAMATION", "HAND", "QUESTION", "OK"])
beep_group = parser.add_mutually_exclusive_group()
beep_group.add_argument("-a", "--asterisk", action="store_true")
beep_group.add_argument("-e", "--exclamation", action="store_true")
beep_group.add_argument("-ha", "--hand", action="store_true")
beep_group.add_argument("-q", "--question", action="store_true")
beep_group.add_argument("-ok", "--ok", action="store_true")
args = parser.parse_args()

if args.asterisk:
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

if args.exclamation:
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)

if args.hand:
    winsound.MessageBeep(winsound.MB_ICONHAND)

if args.question:
    winsound.MessageBeep(winsound.MB_ICONQUESTION)

if args.ok:
    winsound.MessageBeep(winsound.MB_OK)
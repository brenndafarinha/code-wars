import sys
from print_helpers import bprint, sprint

commands = {
    "reboot": "Rebooting launch control system.",
    "halt": "Halting all systems.",
}

try:
    command = sys.argv[1]
except IndexError:
    bprint.upper_print("No command provided. Terminating.")
    sys.exit(1)
else:
    sprint.tacky_print(commands.get(command, "Doing absolutely nothing."))

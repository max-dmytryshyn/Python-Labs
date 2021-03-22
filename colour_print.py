from enum import Enum


class BColors(Enum):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def colour_print(text, colour):
    if colour == 'OKBLUE':
        string = BColors.OKBLUE.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'HEADER':
        string = BColors.HEADER.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'OKCYAN':
        string = BColors.OKCYAN.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'OKGREEN':
        string = BColors.OKGREEN.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'WARNING':
        string = BColors.WARNING.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'FAIL':
        string = BColors.HEADER.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'BOLD':
        string = BColors.BOLD.value + text + BColors.ENDC.value
        print(string)
    elif colour == 'UNDERLINE':
        string = BColors.UNDERLINE.value + text + BColors.ENDC.value
        print(string)

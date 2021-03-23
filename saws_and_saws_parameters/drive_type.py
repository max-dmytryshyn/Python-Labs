from enum import Enum, unique


@unique
class DriveType(Enum):
    MECHANICAL = 1
    ELECTRIC = 2
    INTERNAL_COMBUSTION_ENGINE = 3

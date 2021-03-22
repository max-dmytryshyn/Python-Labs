from saws_and_saws_parameters.saw import Saw
from saws_and_saws_parameters.drive_type import DriveType
from saws_and_saws_parameters.saw_material import SawMaterial
from enum import Enum


class SortOrder(Enum):
    ASC = 0
    DESC = 1


class SawManager:
    def __init__(self):
        self.__saws = []

    @property
    def saws(self):
        return self.__saws

    def add_saw(self, saw=Saw()):
        self.__saws.append(saw)

    def remove_saw_by_index(self, index=0):
        self.__saws.pop(index)

    def clear_saws_list(self):
        self.__saws.clear()

    def search_by_drive_type(self, drive_type = DriveType.MECHANICAL):
        found_saws = [saw for saw in self.__saws if saw.drive_type == drive_type]
        return found_saws

    def search_by_made_of_material(self, made_of_material = SawMaterial()):
        found_saws = [saw for saw in self.__saws if saw.made_of_material == made_of_material]
        return found_saws

    def sort_by_length(self, saws=[], sort_order = SortOrder.ASC):
        saws.sort(reverse = sort_order.value, key = lambda saw: saw.length_in_cm)
